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
API_URL = "https://router.huggingface.co/hf-inference/models/sentence-transformers/all-MiniLM-L6-v2/pipeline/feature-extraction"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

app = FastAPI(title="Faculty Finder API")

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
            requests.get("https://faculty-connect.onrender.com/", timeout=10)
        except:
            pass
        time.sleep(600)

threading.Thread(target=keep_alive, daemon=True).start()

# --- LOAD DATA ---
print("Loading Faculty Data...")
try:
    with open("faculty_data.pkl", "rb") as f:
        data = pickle.load(f)
        df = data['dataframe']
        # Convert to numpy array immediately for speed
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
            
            if isinstance(result, dict) and "estimated_time" in result:
                time.sleep(result.get("estimated_time", 5))
                continue
            
            # 🛡️ THE FLATTENING FIX
            # Hugging Face can return [[[...]]] or [[...]] or [...]
            res = np.array(result)
            return res.flatten().tolist() # This guarantees a single flat list of numbers
            
        except Exception as e:
            print(f"Retry {i+1} failed: {e}")
            time.sleep(2)
    return None

class SearchRequest(BaseModel):
    query: str

@app.post("/search")
async def search_faculty(request: SearchRequest):
    if df is None:
        raise HTTPException(status_code=500, detail="Database not loaded")

    try:
        raw_output = query_hf_api(request.query)
        if raw_output is None:
            return {"results": [], "message": "AI Service Timeout"}

        query_vector = np.array(raw_output)

        # 🎯 MATH CHECK: Ensure dimensions match
        if query_vector.shape[0] != embeddings.shape[1]:
            print(f"Mismatch! Query vector is {query_vector.shape[0]}, but DB expects {embeddings.shape[1]}")
            # If this prints, you need to re-generate your faculty_data.pkl
            return {"results": [], "message": "Model dimension mismatch."}

        # Calculate Scores
        scores = np.dot(embeddings, query_vector)
        sorted_indices = np.argsort(scores)[::-1]

        results = []
        for idx in sorted_indices[:15]:
            current_score = float(scores[idx])
            # Set to a very low number to force matches to show up during debugging
            if current_score < -100: break 

            faculty_data = df.iloc[idx]
            results.append({
                "name": faculty_data.get("Name", "Unknown"),
                "specialization": faculty_data.get("Specialization", "N/A"),
                "image_url": faculty_data.get("Image_URL", ""),
                "profile_url": faculty_data.get("Profile_URL", ""),
                "teaching": faculty_data.get("Teaching", "N/A"),
                "publications": faculty_data.get("Publications", "N/A"),
                "score": round(current_score, 4)
            })

        print(f"✅ Successfully found {len(results)} matches for '{request.query}'")
        return {"results": results}

    except Exception as e:
        print(f"❌ Search Crash: {e}")
        return {"results": [], "message": f"Calculation error: {str(e)}"}

@app.get("/")
def home():
    return {"message": "API is online!"}
