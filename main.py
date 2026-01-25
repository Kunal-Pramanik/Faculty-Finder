from fastapi import FastAPI
from sqlalchemy import create_engine, text
from pydantic import BaseModel
from typing import List, Optional

# SQLite connection
DATABASE_URL = "sqlite:///faculty.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

app = FastAPI(title="Faculty API (SQLite)")

class FacultyResponse(BaseModel):
    faculty_id: str
    name: str
    profile_url: Optional[str]
    education: Optional[str]
    email: Optional[str]
    contact_number: Optional[str]
    research_area: Optional[str]

@app.get("/faculty", response_model=List[FacultyResponse])
def get_faculty():
    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT
                    faculty_id,
                    name,
                    profile_url,
                    education,
                    email,
                    contact_number,
                    research_area
                FROM faculty
                ORDER BY faculty_id
            """)
        )
        return result.mappings().all()
