import streamlit as st
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="DocMind AI - PDF Chatbot",
    layout="wide"
)

st.title("📘 DocMind AI")
st.caption("Chat with your PDFs • Fully Offline • Phi-3 • FAISS")


# ---------------- SESSION STATE ----------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "llm" not in st.session_state:
    st.session_state.llm = Ollama(
        model="phi3",
        temperature=0
    )


# ---------------- CACHE EMBEDDINGS ----------------

@st.cache_resource
def load_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


# ---------------- PROCESS PDF ----------------

def process_pdf(file):

    os.makedirs("data", exist_ok=True)
    pdf_path = os.path.join("data", file.name)

    with open(pdf_path, "wb") as f:
        f.write(file.getbuffer())

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    if not documents:
        return None

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    embeddings = load_embeddings()

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vectorstore


# ---------------- SIDEBAR ----------------

st.sidebar.header("📂 Upload PDF")

uploaded_file = st.sidebar.file_uploader(
    "Upload a PDF file",
    type=["pdf"]
)


# ---------------- LOAD PDF ----------------

if uploaded_file:

    with st.spinner("📖 Processing PDF..."):

        vectorstore = process_pdf(uploaded_file)

        if vectorstore is None:
            st.error("❌ No readable text found in PDF.")
            st.stop()

        st.session_state.vectorstore = vectorstore
        st.session_state.chat_history = []

        st.success("✅ PDF processed successfully!")


# ---------------- DISPLAY CHAT HISTORY ----------------

for role, message in st.session_state.chat_history:
    st.chat_message(role).write(message)


# ---------------- USER INPUT ----------------

if st.session_state.vectorstore:

    user_query = st.chat_input("Ask a question about the PDF")

    if user_query:

        st.chat_message("user").write(user_query)

        with st.spinner("🤔 Thinking..."):

            try:

                docs = st.session_state.vectorstore.similarity_search(
                    user_query,
                    k=3
                )

                context = "\n\n".join(
                    [doc.page_content for doc in docs]
                )

                prompt = f"""
You are an intelligent assistant.

Answer the question using ONLY the context below.
If the answer is not in the context, say:
"I could not find this information in the document."

Context:
{context}

Question:
{user_query}
"""

                answer = st.session_state.llm.invoke(prompt)

            except Exception as e:

                st.error(
                    "⚠️ Ollama is not running.\n\nRun this command in terminal:\n\nollama serve"
                )

                st.stop()

        st.chat_message("assistant").write(answer)

        st.session_state.chat_history.append(
            ("user", user_query)
        )

        st.session_state.chat_history.append(
            ("assistant", answer)
        )


else:

    st.info("⬅ Upload a PDF to start chatting.")