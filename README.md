# 📚 AI-Powered Personal Study Assistant

**Description**:  
AI-powered study assistant that extracts topics from notes using NLP, generates flashcards/quizzes, and schedules smart revisions with spaced repetition. Built with Flask and React, it helps students plan, review, and retain information more effectively.

## 🚀 Features
- Upload notes or PDFs
- Extract key topics using NLP (spaCy or BERT)
- Automatically generate flashcards and quizzes
- Schedule reviews with spaced repetition or RL
- User-friendly web interface (React + Flask API)

## 🧠 Technologies Used
- Python, Flask
- React.js
- spaCy / HuggingFace Transformers
- PyMuPDF (PDF text extraction)
- PostgreSQL or MongoDB (data storage)

## 🛠 Setup Instructions

### Backend (Flask)
```bash
git clone https://github.com/EvansCortez/study-assistant.git
cd study-assistant/backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
