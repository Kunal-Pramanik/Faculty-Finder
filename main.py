from fastapi import FastAPI
from sqlalchemy import create_engine, text
from pydantic import BaseModel
from typing import List, Optional

username = "postgres"
password = "0987"
host = "localhost"
port = "5432"
database = "Faculty_finder"

engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

app = FastAPI(title="Faculty API")

class FacultyResponse(BaseModel):
    faculty_id: str
    name: str
    education: Optional[str]
    research_interests: Optional[str]
    profile_url: Optional[str]
    clean_text: Optional[str]

@app.get("/faculty", response_model=List[FacultyResponse])
def get_faculty():
    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT
                    faculty_id,
                    name,
                    education,
                    research_interests,
                    profile_url,
                    clean_text
                FROM faculty_list.faculty
                ORDER BY faculty_id
            """)
        )
        return result.mappings().all()

