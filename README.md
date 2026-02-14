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
- [Key Technical Expertise](#key-technical-expertise)
- [Project Structure](#project-structure)
- [Pipeline Workflow](#pipeline-workflow)
- [Data Schema & Engineering](#data-schema--engineering)
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

## <a id="why-semantic-search"></a>💡 Why Semantic Search?

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

## <a id="tech-stack"></a>🛠️ Tech Stack

The system is built using a modern, decoupled architecture to handle the requirements of data engineering and real-time AI inference.

### 🏗️ Backend & Data Engineering
* **Python 3.10+**: The core language for the entire data lifecycle and API development.
* **FastAPI**: A high-performance, asynchronous web framework used to serve search results with minimal latency.
* **BeautifulSoup4**: The primary tool for the automated scraping pipeline, handling complex and inconsistent HTML layouts.
* **Pandas & NumPy**: Used for rigorous data cleaning, ETL processes, and optimized matrix-based similarity calculations.
* **SQLite**: A lightweight relational database for persistent metadata storage.

### 🤖 Artificial Intelligence & NLP
* **Sentence-Transformers**: Specifically the `all-MiniLM-L6-v2` model, used to map research text into 384-dimensional semantic vectors.
* **Hugging Face Inference API**: Provides a scalable cloud environment for real-time model inference without heavy local resource usage.
* **Pickle (Serialization)**: Used to store and instantly load pre-computed vector embeddings for production speed.

### 🖥️ Frontend & UX
* **Next.js 14**: A modern React framework used for a responsive, "zero-build" user interface.
* **Tailwind CSS**: Utility-first styling used to create a professional, dark-themed academic dashboard.
* **Lucide React**: For high-quality, lightweight vector iconography.
---

## <a id="key-technical-expertise"></a>🧠 Key Technical Expertise

### 🛠️ Data Engineering & ETL
* **Automated Ingestion**: Developed a resilient multi-source scraper using **BeautifulSoup4** for deep metadata extraction.
* **Pipeline Architecture**: Engineered a modular ETL workflow for text normalization and email de-obfuscation.
* **Relational Storage**: Architected a dual-persistence layer using **SQLite** and **Pickle** for high-speed retrieval.

### 🤖 AI & Semantic Discovery
* **Neural Vectorization**: Leveraged **Transformers** (`all-MiniLM-L6-v2`) to map expertise into a 384-dimensional space.
* **Optimized Retrieval**: Implemented high-concurrency similarity ranking using **NumPy** matrix operations.
* **Contextual Matching**: Solved the "keyword gap" by enabling intent-based discovery.

### 🌐 Full-Stack Deployment
* **Asynchronous Backend**: Built a high-performance **FastAPI** engine for real-time inference.
* **Modern Frontend**: Developed a responsive dashboard using **Next.js 14** and **Tailwind CSS**.
* **Cloud Infrastructure**: Orchestrated a decoupled deployment on **Render** and **Vercel** with integrated resilience.

---
## <a id="project-structure"></a>📂 Project Structure

```bash
Connect2Faculty/
├── backend/                  # FastAPI Production Server
│   ├── main.py               # API logic & Semantic Retrieval
│   ├── faculty_data.pkl      # Serialized vector database
│   └── requirements.txt      # Backend dependencies
├── data_pipeline/            # Data Engineering & ETL Module
│   ├── scrapy.py             # BeautifulSoup4 Scraper
│   ├── data_preprocessing.py # Text normalization & Email de-obfuscation
│   ├── data_push_db.py       # SQL table creation & data loading
│   ├── faculty.db            # SQLite metadata storage
│   └── data.ipynb            # EDA & Data Statistics
├── frontend/                 # Next.js 14 Web Application
│   ├── src/app/page.tsx      # Semantic search UI
│   └── tailwind.config.ts    # Custom styling
└── README.md                 # Project documentation
```

---
## <a id="pipeline-workflow"></a>🔄 Pipeline Workflow

The project implements a resilient ETL pipeline that automates the transition from raw web sources to a structured AI database.

### 📥 1. Extraction (scrapy.py)
* **Targeted Crawling**: Scrapes 5 categories of faculty directories for 100% coverage.
* **Deep Scrape**: Navigates into individual profile links to extract biographies and publications.
* **Resilience**: Integrated 1s delays and custom headers to ensure stable ingestion.

### 🔄 2. Transformation (data_preprocessing.py)
* **Text Normalization**: Regex-based cleaning of research interests for high-quality embeddings.
* **Email De-obfuscation**: Automated recovery of contact details from web-protected formats.
* **Integrity Filters**: Drops incomplete records and maps standardized Faculty IDs (F-XXX).

### 📤 3. Loading (data_push_db.py)
* **Metadata Persistence**: Structured data is committed to a relational SQLite database.
* **Vector Serialization**: Pre-computed embeddings are stored in a Pickle (.pkl) file for O(1) loading.

---

## <a id="data-schema--engineering"></a>🗄️ Data Schema & Engineering

The system utilizes a dual-storage strategy: a relational **SQLite** database(`faculty.db`) for structured metadata and a serialized **Pickle** vector store for high-speed AI retrieval.

### 📊 Database Schema (faculty table)

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| **faculty_id** | `TEXT (PK)` | Unique identifier (e.g., F-001). |
| **Name** | `TEXT` | Full name of the faculty member. |
| **Email** | `TEXT` | De-obfuscated contact address. |
| **Specialization** | `TEXT` | Primary academic domain. |
| **Research_Interests**| `TEXT` | Normalized text for vector embeddings. |
| **Qualification** | `TEXT` | Academic background. |
| **Profile_URL** | `TEXT` | Link to institutional profile. |
| **Image_URL** | `TEXT` | Path to profile image. |

### ⚙️ Engineering Highlights
* **Primary Key Indexing**: Optimized `faculty_id` for fast metadata retrieval.
* **Data Normalization**: Cleaned and standardized all text inputs during the ETL process.
* **Hybrid Storage**: Combined SQL for relational data with Pickle for high-dimensional vector math.

---
## <a id="semantic-search--vector-retrieval"></a>🧠 Semantic Search & Vector Retrieval

Unlike traditional search, Connect2Faculty understands the **intent** behind your query using high-dimensional vector math.

### 1. Neural Representation
* **Model**: Sentence-Transformers `all-MiniLM-L6-v2`.
* **Latent Space**: Maps research interests into a **384-dimensional space**.
* **Semantic Awareness**: Recognizes conceptual relationships between varied academic terminologies.

### 2. Retrieval Engine
* **Real-time Inference**: Queries are vectorized via **Hugging Face Inference API**.
* **Mathematical Ranking**: Uses **NumPy-powered Cosine Similarity** to calculate the distance between user intent and faculty expertise.
* **Production Speed**: Pre-computed embeddings in **Pickle** format allow for sub-millisecond search performance.

---
## <a id="data-intelligence--statistics"></a>📊 Data Intelligence & Statistics

Derived from the comprehensive EDA performed in `data_pipeline/eda.ipynb` on the raw scraped dataset (112 initial records).

### 📈 Global Dataset Insights
* **Education Quality**: 84.82% of faculty hold a PhD.
* **Research Productivity**: Average of 7.41 publications per faculty.
* **Information Density**: 97.32% have teaching information available.

### 📉 Full Column-wise Data Quality (Null Analysis)

| Column Name | Null Count | Null % | System Significance |
| :--- | :--- | :--- | :--- |
| **Name** | 0 | 0.00% | Primary UI identifier. |
| **Profile URL** | 0 | 0.00% | Foundation for deep-crawling. |
| **Qualification** | 2 | 1.79% | Academic background context. |
| **Email** | 1 | 0.89% | Core contact point for students. |
| **Specialization** | 0 | 0.00% | Secondary search anchor. |
| **Image URL** | 0 | 0.00% | Visual profile representation. |
| **Research Interests**| 93 | 83.04% | Primary vector embedding source. |
| **Publications** | 44 | 39.29% | Research output context. |

### 🧠 Semantic Retrieval Intelligence
* **Index Pruning**: Final index consists of 109 verified profiles for maximum search integrity.
* **Vector Coverage**: 100% of specialization data was mapped to 384-dimensional latent space.
* **Scraping Excellence**: 100% success rate on Image and Profile URL extraction.

---
