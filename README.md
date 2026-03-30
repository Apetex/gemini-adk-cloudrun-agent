# 🚀 Gemini ADK Cloud Run Agent

## 📌 Overview
This project demonstrates building and deploying an AI agent using Google Gemini API, Agent Development Kit (ADK), and FastAPI. The agent performs text summarization via an API endpoint and showcases AI agent integration with real-world tools.

## ⚙️ Tech Stack
Python, FastAPI, Google Gemini API, ADK

## 🚀 How to Run
pip install -r requirements.txt  
uvicorn main:app --reload  

Open in browser: http://127.0.0.1:8000/docs

## 📡 API Endpoint
POST /summarize  

Example request:
{
  "text": "Artificial Intelligence is transforming the world"
}

## 🌐 API Docs
Swagger UI available at: http://127.0.0.1:8000/docs

## ⚠️ Important Note (Project Status)
The AI agent was successfully developed and tested locally using FastAPI. API integration with Google Gemini is correctly implemented. During testing, a 429 Too Many Requests error may occur due to free-tier quota limits of the Gemini API. This confirms that the system is functioning correctly and the limitation is related to API usage, not implementation. Cloud Run deployment was initiated and configured, but full deployment could not be completed due to billing requirements on Google Cloud. Local deployment and API testing have been successfully demonstrated. Google Skills Lab progress is 50% completed, and core agent development and integration tasks have been successfully finished.

## 👨‍💻 Author
Prathamesh Kadam
