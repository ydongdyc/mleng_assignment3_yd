# 📰 Headline Sentiment Analyzer (Assignment 3)

This project is a full-stack application for sentiment analysis of news headlines, built as part of a machine learning assignment. It consists of:
- A **FastAPI** backend service that scores headline sentiment using a pretrained SVM model.
- A **Streamlit** frontend interface that allows users to input, modify, and submit headlines to the backend and view sentiment predictions.

---

## 🚀 Features
- Interactive UI for editing/deleting headlines
- Real-time sentiment scoring via API
- Supports batch headline submission
- Clean and simple user experience

---

## 📁 Project Structure

```
mleng_assignment3_yd/
├── streamlit_app.py         # Streamlit frontend app
├── score_headlines_api.py   # FastAPI backend service
├── svm_model.joblib         # Pretrained SVM sentiment classifier
```

---

## ⚙️ Requirements

Make sure you have Python 3.8+ installed. Then install dependencies using:

```bash
pip install fastapi uvicorn streamlit sentence-transformers scikit-learn joblib requests
```

---

## 🧪 Local Setup Instructions

### 1. Clone the Repository
```bash
cd mleng_assignment3_yd
```

### 2. Run the FastAPI Backend (Assignment 2)
```bash
uvicorn score_headlines_api:app --host 0.0.0.0 --port 8001
```

Check it's running: http://localhost:8001/status should return `{"status": "OK"}`

### 3. Run the Streamlit Frontend (Assignment 3)
Open a **new terminal** and run:
```bash
streamlit run streamlit_app.py --server.port 9081
```

Visit the UI at: http://localhost:9081

---

## 📸 Example UI

![App Screenshot](screenshot.png) <!-- Replace with actual image if you upload -->

---

## ✅ To-Do / Enhancements
- Add sentiment-based color badges (green/gray/red)
- Display sentiment distribution chart
- Deploy to cloud (Render, Replit, or AWS)
- Export results to CSV

---

## 📄 License
This is a student project for educational purposes.

---
