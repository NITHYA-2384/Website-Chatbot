# Website-Based Chatbot with Voice Support

## Overview
This project is an intelligent chatbot that answers user queries based on the content of a specific website.  
It uses a **retrieval-based approach (RAG)** to provide accurate and context-aware responses instead of generating random answers.

The chatbot features a modern UI, voice interaction, and works completely offline without requiring paid APIs.

---

## Features

- ChatGPT-style conversational interface
- Website-specific question answering
- Vector-based semantic search using FAISS
- Voice input (Speech-to-Text)
- Voice output (Text-to-Speech)
- Typing animation for better user experience
- Stop voice control functionality
- Fully offline solution (no API dependency)

---

## How It Works

1. Website content is collected and stored in a text file  
2. The content is split into smaller chunks  
3. Each chunk is converted into vector embeddings using TF-IDF  
4. Embeddings are stored in a FAISS vector database  
5. When a user asks a question:
   - The query is converted into a vector  
   - Similar content is retrieved  
   - The most relevant answer is returned  

---

## Technologies Used

- Python  
- Streamlit (User Interface)  
- Scikit-learn (TF-IDF Vectorization)  
- FAISS (Vector Database)  
- SpeechRecognition(image.png) (Voice Input)  
- pyttsx3 (Voice Output)  

---

##  Project Structure
website-chatbot/
│
├── app.py # Main application (UI + voice + chatbot)
├── backend.py # Embedding + vector search logic
├── text_splitter.py # Text processing and chunking
├── scraper.py # Website data extraction
├── requirements.txt # Project dependencies
│
└── data/
└── website_data.txt # Stored website content
