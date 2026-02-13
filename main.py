from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import pickle
import requests
import os
import time
import threading

HF_TOKEN = os.environ.get("HF_TOKEN") 
API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

app = FastAPI()

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

# Keep-alive to prevent Render sleep
def keep_alive():
    while True:
        try: requests.get("https://faculty-connect.onrender.com/", timeout=10)
        except: pass
        time.sleep(600)

threading.Thread(target=keep_alive, daemon=True).start()

# Load Database
try:
    with open("faculty_data.pkl", "rb") as f:
        data = pickle.load(f)
        df = data['dataframe']
        embeddings = np.array(data['embeddings']) 
except Exception as e:
    print(f"❌ Error: {e}"); df = None


def query_hf_api(text):
    for i in range(3):
        try:
            response = requests.post(API_URL, headers=headers, json={"inputs": text}, timeout=20)
            result = response.json()
            
            # 1. HANDLE MODEL COLD-START
            if isinstance(result, dict) and "error" in result:
                if "loading" in result["error"].lower():
                    wait_time = result.get("estimated_time", 10)
                    print(f"⏳ Model loading... waiting {wait_time}s")
                    time.sleep(wait_time)
                    continue
                return None
            
            # 2. FLATTEN AND VALIDATE DIMENSIONS
            # Hugging Face often returns nested lists like [[[...]]]
            res = np.array(result)
            flat_res = res.flatten().tolist()
            
            if len(flat_res) == 384:
                return flat_res
            else:
                print(f"❌ Dimension Mismatch! Got {len(flat_res)}, expected 384")
                return None
                
        except Exception as e:
            print(f"Retry {i+1} failed: {e}")
            time.sleep(2)
    return None

class SearchRequest(BaseModel):
    query: str

@app.post("/search")
async def search(request: SearchRequest):
    if df is None: raise HTTPException(status_code=500, detail="DB Error")
    
    raw_vector = query_hf_api(request.query)
    if not raw_vector: return {"results": [], "message": "AI Timeout"}

    # Cosine Similarity Calculation
    query_vec = np.array(raw_vector)
    norm_q = query_vec / np.linalg.norm(query_vec)
    norm_e = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
    
    scores = np.dot(norm_e, norm_q)
    indices = np.argsort(scores)[::-1][:15]

    results = []
    for idx in indices:
        if scores[idx] < 0.05: continue
        row = df.iloc[idx]
        results.append({
            "name": row.get("Name", "Unknown"),
            "specialization": row.get("Specialization", "N/A"),
            "image_url": row.get("Image_URL", ""),
            "profile_url": row.get("Profile_URL", ""),
            "score": float(scores[idx])
        })
    return {"results": results}

@app.get("/")
def home(): return {"message": "API is online!"}
