from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, text
from pydantic import BaseModel
from typing import List
import numpy as np

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI(title="Faculty Semantic Recommender")

# ✅ CORS (REQUIRED FOR PUBLIC WEBSITE)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = "sqlite:///faculty.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

model = SentenceTransformer("all-MiniLM-L6-v2")

class RecommendationRequest(BaseModel):
    query: str

class RecommendationResponse(BaseModel):
    faculty_id: str
    name: str
    research_area: str
    score: float

def get_faculty_data():
    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT faculty_id, name, research_area, education
                FROM faculty
                WHERE research_area IS NOT NULL
            """)
        )
        return result.mappings().all()

def semantic_recommend(query: str, top_k: int = 6):
    faculty_data = get_faculty_data()

    faculty_texts = [
        f"{row['research_area']} {row['education']}"
        for row in faculty_data
    ]

    faculty_embeddings = model.encode(faculty_texts)
    query_embedding = model.encode([query])

    similarities = cosine_similarity(query_embedding, faculty_embeddings)[0]

    ranked = sorted(
        zip(faculty_data, similarities),
        key=lambda x: x[1],
        reverse=True
    )

    return [
        {
            "faculty_id": faculty["faculty_id"],
            "name": faculty["name"],
            "research_area": faculty["research_area"],
            "score": round(float(score * 100), 2)
        }
        for faculty, score in ranked[:top_k]
    ]

@app.post("/recommend", response_model=List[RecommendationResponse])
def recommend(request: RecommendationRequest):
    return semantic_recommend(request.query)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "Faculty Semantic Recommender API is running"}
