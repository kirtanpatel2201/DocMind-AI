# 📘 DocMind AI – Conversational PDF Intelligence

**DocMind AI** is an offline **AI-powered PDF conversational assistant** that allows users to interact with documents using natural language.
It transforms static PDF files into interactive knowledge sources by combining semantic search with a local large language model.

The system processes PDF documents, converts text into vector embeddings, retrieves the most relevant information, and generates accurate answers using a locally running AI model.

---

# 🚀 Project Purpose

The purpose of **DocMind AI** is to make document exploration faster and more intelligent. Instead of manually reading large PDF documents, users can simply ask questions and receive answers directly from the document content.

This project demonstrates the use of **Retrieval Augmented Generation (RAG)** to build a fully offline document intelligence system.

---

# 🧠 Key Features

* Chat with any PDF document using natural language
* Fully offline AI system (no API keys required)
* Fast semantic search using vector embeddings
* Local LLM inference using Ollama
* Interactive chat interface built with Streamlit
* Lightweight and easy to deploy locally

---

# 🧰 Technologies Used

* Python
* Streamlit
* LangChain
* FAISS Vector Database
* HuggingFace Sentence Transformers
* Ollama (Local LLM runtime)

---

# ⚙️ Installation Guide

Follow the steps below to run the project locally.

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/kirtanpatel2201/DocMind-AI.git
cd doc_mind
```

---

## 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Project Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Install Ollama

Download and install Ollama from:

https://ollama.com

Start the Ollama service:

```bash
ollama serve
```

---

## 5️⃣ Download the Phi-3 Model

```bash
ollama pull phi3
```

This downloads the local language model used to generate answers.

---

# ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Once the server starts, open your browser and go to:

```
http://localhost:8501
```

Upload a PDF and start asking questions about the document.

---

# 📂 Project Structure

```
docmind-ai
│
├── app.py
│   Main Streamlit application that runs the chatbot interface
│
├── requirements.txt
│   Contains all Python dependencies required to run the project
│
├── README.md
│   Project documentation and usage instructions
│
├── data/
│   Stores uploaded PDF documents temporarily
│
└── assets/
    Optional images, architecture diagrams, or screenshots
```

---

# ⚙️ How the System Works

The system follows a **Retrieval Augmented Generation (RAG)** pipeline:

1. User uploads a PDF file
2. Text is extracted from the document
3. Text is split into smaller chunks
4. Each chunk is converted into vector embeddings
5. FAISS stores these embeddings in a vector database
6. When a question is asked, relevant chunks are retrieved
7. The local Phi-3 model generates an answer based on the retrieved context

---

# 🧪 Example Use Cases

### 📚 Academic Research

Students can quickly search through research papers and textbooks.

### 🧾 Business Documents

Analyze reports, contracts, and documentation efficiently.

### 📑 Legal Document Review

Extract relevant clauses and explanations from long legal PDFs.

### 🏥 Medical Papers

Ask questions about research papers or medical reports.

### 🧑‍💻 Developer Documentation

Quickly search through technical documentation and guides.

---

---

# 📈 Future Improvements

Possible enhancements for the project:

* Support for multiple PDFs at once
* Persistent vector database storage
* Conversation memory support
* Document highlighting of answers
* Web deployment using Docker

---

---

# 👨‍💻 Author

Collaborative
