# ✨ Connect2Faculty – End-to-End Semantic Search System

An end-to-end Big Data Engineering (BDE) pipeline and semantic search platform.

Developed a custom crawler to scrape and clean university faculty data, implemented a high-dimensional vector search engine using FastAPI and Hugging Face transformers, and deployed a responsive Next.js frontend for real-time AI-powered mentor discovery.

---

## 🚀 Live System
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

## Overview
Connect2Faculty is an intelligent faculty discovery platform that enables **semantic, intent-based search** over university faculty profiles, going beyond traditional keyword matching.

---

## Why Semantic Search?

Keyword-based search relies on exact word matching and fails when user intent and terminology differ. In academic discovery, the same research area is often described using varied or specialized language.

Semantic search captures the **meaning and context** of queries and documents using vector embeddings, enabling intent-aware retrieval and robust handling of synonyms.

**Example:**  
A user searching *“I want to work on GenAI”* can correctly retrieve faculty profiles mentioning *“large language models”*, *“deep learning”*, or *“artificial intelligence”*, even when the exact term *“GenAI”* is absent.

As a result, semantic search provides more accurate faculty matching and a significantly improved search experience compared to traditional keyword search.

---

## System Architecture
- Web scraping & ingestion pipeline
- Data cleaning and normalization
- SQLite-backed API layer
- Transformer-based embedding generation
- Vector similarity search
- Cloud-hosted frontend and backend services

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
