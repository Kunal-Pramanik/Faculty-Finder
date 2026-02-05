# Faculty Finder – Semantic Recommendation System

## Overview

Faculty Finder is an end-to-end **Data Engineering and Data Science project** that builds a structured faculty dataset from university web pages and provides a **semantic faculty recommendation system**.

The system allows users to enter a **free-text research description** and returns the **most relevant faculty members** based on semantic similarity between the query and faculty research profiles.

---

## Problem Statement

Faculty information is typically scattered across multiple web pages in semi-structured HTML format, making it difficult to identify the right faculty member for collaboration, guidance, or referral.

The objectives of this project are to:

- Crawl and collect faculty profile data from university websites
- Clean and normalize unstructured HTML data
- Store faculty information in a relational database
- Build a **semantic recommender system** using the processed data
- Expose the recommender via an API that can be consumed by a public website

---

## System Architecture

```
Faculty Web Pages (HTML)
        ↓
Data Ingestion (Web Scraping)
        ↓
Data Cleaning & Normalization
        ↓
SQLite Database (faculty.db)
        ↓
Semantic Recommender (Embeddings + Similarity)
        ↓
FastAPI Backend
        ↓
Public Website / Client Application
```

---

## Tech Stack

- **Programming Language:** Python
- **Web Scraping:** Requests, BeautifulSoup
- **Data Processing:** Pandas
- **Database:** SQLite
- **ORM / DB Access:** SQLAlchemy
- **Machine Learning / NLP:** Sentence Transformers, Scikit-learn
- **API Framework:** FastAPI
- **Deployment:** Railway (Backend), GitHub Pages / Vercel (Frontend)
- **API Documentation:** OpenAPI (Swagger)

---

## Dataset Description

The dataset contains structured faculty information with the following fields:

| Column          | Description |
|-----------------|------------|
| faculty_id      | Unique faculty identifier |
| name            | Faculty name |
| profile_url     | Faculty profile webpage |
| education       | Educational background |
| email           | Email address |
| contact_number  | Contact number |
| research_area   | Research interests |
| photo           | photo_url of faculty photo |

---

## Semantic Faculty Recommender System

### Overview

This project includes a **content-based semantic recommender system** that identifies suitable faculty members based on a user's research interest description.

Unlike keyword-based search, this system understands the **semantic meaning** of text using embeddings.

---

### Recommendation Algorithm

1. Faculty research areas and education details are combined into a single textual representation.
2. These texts are converted into dense vector embeddings using a **Sentence Transformer model** (`all-MiniLM-L6-v2`).
3. The user query is embedded using the same model.
4. **Cosine similarity** is calculated between the query embedding and faculty embeddings.
5. Faculty members are ranked by similarity score.
6. The top-ranked faculty members are returned as recommendations.

This enables semantic matching such as:
- *"Large Language Models"* → *Natural Language Processing*
- *"Statistical learning"* → *Machine Learning*

---

## API Endpoints

### Semantic Recommendation Endpoint

**Endpoint**
```
POST /recommend
```

**Request Body**
```json
{
  "query": "I want to work in machine learning and data science"
}
```

**Response (Example)**
```json
[
  {
    "faculty_id": "F-1021",
    "name": "Dr. XYZ",
    "research_area": "Machine Learning, Data Mining",
    "score": 87.45
  }
]
```

---

### Health Check

```
GET /health
```

Returns the API status.

---

## How to Run Locally

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the API

```bash
python -m uvicorn main:app --reload
```

### 3. Access API

- API Base URL: `http://127.0.0.1:8000`
- Swagger Docs: `http://127.0.0.1:8000/docs`

---

## Deployment

- The FastAPI backend is deployed as a **public API** using **Railway**.
- CORS is enabled to allow browser-based frontend applications.
- A lightweight frontend can consume the `/recommend` endpoint to provide a **public faculty search website**.

---

## Evaluation Strategy

Since no labeled ground-truth data exists, evaluation is performed qualitatively by:

- Testing multiple research queries
- Inspecting relevance of ranked faculty results
- Verifying semantic consistency across paraphrased queries

---

## Future Enhancements

- Precompute and cache faculty embeddings for faster response
- Store embeddings in a vector database
- Add faculty profile images and links in frontend
- Implement feedback-based ranking
- Extend to multi-university datasets

---

## Author

**Kunal Pramanik**  
MSc Data Science

