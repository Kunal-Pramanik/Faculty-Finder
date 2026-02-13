from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np
import pickle
import requests
import os
import time
import threading

# 🔒 SECURE WAY: Read from Environment Variable
HF_TOKEN = os.environ.get("HF_TOKEN") 
API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

app = FastAPI(title="Faculty Finder API")

# Optimized CORS for your Vercel frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 🚀 KEEP-ALIVE ---
def keep_alive():
    while True:
        try:
            # Self-ping to prevent Render sleep
            requests.get("https://faculty-connect.onrender.com/", timeout=10)
        except:
            pass
        time.sleep(600) # 10 minutes

threading.Thread(target=keep_alive, daemon=True).start()

# --- LOAD DATA ---
print("Loading Faculty Data...")
try:
    with open("faculty_data.pkl", "rb") as f:
        data = pickle.load(f)
        df = data['dataframe']
        embeddings = np.array(data['embeddings']) 
    print(f"✅ Data Loaded! Embeddings shape: {embeddings.shape}")
except Exception as e:
    print(f"❌ Error loading data: {e}")
    df = None

def query_hf_api(text):
    for i in range(3):
        try:
            response = requests.post(API_URL, headers=headers, json={"inputs": text}, timeout=20)
            result = response.json()
            
            # 1. HANDLE MODEL LOADING
            if isinstance(result, dict) and "error" in result:
                if "loading" in result["error"].lower():
                    wait_time = result.get("estimated_time", 10)
                    print(f"⏳ Model loading... waiting {wait_time}s")
                    time.sleep(wait_time)
                    continue
                return None
            
            # 2. FLATTEN AND VALIDATE VECTOR
            res = np.array(result)
            flat_res = res.flatten().tolist()
            
            if len(flat_res) == 384:
                return flat_res
            else:
                print(f"❌ Mismatch! Got {len(flat_res)}, expected 384")
                return None
                
        except Exception as e:
            print(f"Retry {i+1} failed: {e}")
            time.sleep(2)
    return None

class SearchRequest(BaseModel):
    query: str

@app.post("/search")
async def search_faculty(request: SearchRequest):
    if df is None or embeddings is None:
        raise HTTPException(status_code=500, detail="Database not loaded")

    try:
        raw_output = query_hf_api(request.query)
        if raw_output is None:
            return {"results": [], "message": "AI Service Timeout. Try again in 10s."}

        query_vector = np.array(raw_output)

        # Ensure query_vector is 1D for dot product
        if query_vector.ndim > 1:
            query_vector = query_vector.flatten()

        # Calculate Cosine Similarity (Dot product on normalized vectors)
        # We normalize to ensure the score is between 0 and 1 for the UI
        norm_query = query_vector / np.linalg.norm(query_vector)
        norm_embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
        
        scores = np.dot(norm_embeddings, norm_query)
        sorted_indices = np.argsort(scores)[::-1]

        results = []
        for idx in sorted_indices[:15]:
            current_score = float(scores[idx])
            
            # Filter out very poor matches
            if current_score < 0.1: continue 

            faculty_data = df.iloc[idx]
            results.append({
                "name": faculty_data.get("Name", "Unknown"),
                "specialization": faculty_data.get("Specialization", "N/A"),
                "image_url": faculty_data.get("Image_URL", ""),
                "profile_url": faculty_data.get("Profile_URL", ""),
                "score": current_score # Next.js frontend will multiply by 100
            })

        print(f"✅ Found {len(results)} matches for '{request.query}'")
        return {"results": results}

    except Exception as e:
        print(f"❌ Search Crash: {e}")
        return {"results": [], "message": f"Server Error: {str(e)}"}

@app.get("/")
def home():
    return {"message": "API is online!", "status": "Ready"}
