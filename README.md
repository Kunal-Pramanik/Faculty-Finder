# ✨ Connect2Faculty – End-to-End Semantic Faculty Search System

An end-to-end Big Data Engineering (BDE) pipeline and semantic search platform.

Developed a custom crawler to scrape and clean university faculty data, implemented a high-dimensional vector search engine using FastAPI and Hugging Face transformers, and deployed a responsive Next.js frontend for real-time AI-powered mentor discovery.

---

## 🟢 Live System
**Hosted on Vercel & Render** 👉 [https://faculty-connect-data-riders-pi.vercel.app](https://faculty-connect-data-riders-pi.vercel.app/)

---

## 📑 Table of Contents

- [Overview](#overview)
- [Why Semantic Search?](#why-semantic-search)
- [System Architecture](#system-architecture)
- [Tech Stack](#tech-stack)
- [Skills Demonstrated](#skills-demonstrated)
- [Data Schema & Engineering](#data-schema--engineering)
- [Project Structure](#project-structure)
- [Pipeline Workflow](#pipeline-workflow)
- [Semantic Search & Vector Retrieval](#semantic-search--vector-retrieval)
- [Data Intelligence & Statistics](#data-intelligence--statistics)
- [API Usage & Documentation](#api-usage--documentation)
- [Frontend Features & UI/UX](#frontend-features--uiux)
- [Screenshots & Live Demos](#screenshots--live-demos)
- [Installation & Setup](#installation--setup)
- [Cloud Deployment & Resilience](#cloud-deployment--resilience)
- [Help & Troubleshooting](#help--troubleshooting)
- [The Data Riders Team](#the-data-riders-team)

---

## <a id="overview"></a>🚀 Overview

**Connect2Faculty** is an intelligent faculty discovery platform that enables **semantic, intent-based search** over university faculty profiles, going beyond traditional keyword matching. 

### 💡 The Problem & Solution
Traditional search systems fail when terminology differs. A student searching for **"Financial Prediction"** might miss an expert listed under **"Stochastic Portfolio Theory"**. Connect2Faculty solves this by mapping research ideas into a shared **384-dimensional semantic vector space**, recognizing conceptual relationships between modern research terms and foundational specializations.

### 🔄 System Workflow
1. **Scrape & Ingest**: Automated crawling of faculty profiles using **BeautifulSoup4**.
2. **Clean & Transform**: Advanced text normalization and email de-obfuscation via **Pandas**.
3. **Embed & Index**: Generation of dense vector representations using **Hugging Face Transformers**.
4. **Search & Rank**: High-speed **Cosine Similarity** retrieval powered by **NumPy** and **FastAPI**.

---

## <a id="Why Semantic Search?"></a>🔶 Why Semantic Search?

Keyword-based search relies on exact word matching and fails when user intent and terminology differ. In academic discovery, the same research area is often described using varied or specialized language.

Semantic search captures the **meaning and context** of queries and documents using vector embeddings, enabling intent-aware retrieval and robust handling of synonyms.

**Example:**  
A user searching *“I want to work on GenAI”* can correctly retrieve faculty profiles mentioning *“large language models”*, *“deep learning”*, or *“artificial intelligence”*, even when the exact term *“GenAI”* is absent.

As a result, semantic search provides more accurate faculty matching and a significantly improved search experience compared to traditional keyword search.

---

## <a id="system-architecture"></a> ⚙️ System Architecture

The project follows a modular, decoupled architecture to separate the heavy data engineering pipeline from the real-time AI inference and user interface.

```text
[ Web Sources: DA-IICT Faculty Directories ]
           ↓
[ Data Pipeline: scrapy.py → data_preprocessing.py → data_push_db.py ]
           ↓
[ Relational Storage: SQLite DB (faculty.db) ]
           ↓
[ AI Model Service: Hugging Face Router API → all-MiniLM-L6-v2 ]
           ↓
[ Production Backend: FastAPI (main.py + faculty_data.pkl) ]
           ↓
[ Frontend UI: Next.js 14 (Tailwind CSS + Lucide React) ]
```
---

## Tech Stack
- **Backend:** Python, FastAPI
- **Database:** SQLite
- **Search:** Transformer embeddings, cosine similarity
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Vercel (UI), Render (API)
- **Data Engineering:** Pandas, automated pipelines

---

## Skills Demonstrated
- Big Data Engineering fundamentals
- Semantic search & NLP
- Backend API design
- Database schema design
- End-to-end system integration
- Cloud deployment & scalability

---

## Data Schema & Engineering
- Faculty metadata storage
- Research interest normalization
- Efficient indexing for fast retrieval
- Clean, query-ready data pipelines

---

## Project Structure
```text
Connect2Faculty/
├── backend/
├── frontend/
├── data/
├── embeddings/
├── api/
└── README.md
