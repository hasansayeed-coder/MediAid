import os
from pathlib import Path
from langchain_community.vectorstores import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from .pdf_loader import load_pdf_documents

PROJECT_ROOT = Path(__file__).parent.parent.resolve()

DATA_DIR = PROJECT_ROOT / "data"
VECTOR_DB_DIR = PROJECT_ROOT / "medical_db"
PDF_PATH = DATA_DIR / "medical_book.pdf"

_embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
_vectorstore = Nones

def initialize_vectorstore() : 
    global _vectorstore

    if _vectorstore is None:
        os.makedirs(DATA_DIR , exist_ok=True)
        os.makedirs(VECTOR_DB_DIR , exist_ok=True)

        if not PDF_PATH.exists() : 
            raise FileNotFoundError(f"PDF file not found at {PDF_PATH}")
        
        #load and process documents

        doc_splits = load_pdf_documents(str(PDF_PATH))

        _vectorstore = Chroma.from_documents(
            documents = doc_splits , 
            _embeddings=_embeddings , 
            persist_directory=str(VECTOR_DB_DIR) , 
            collection_metadata={"hnsw : space" : "cosine"}
        )
    return _vectorstore

def get_retriever() : 
    if _vectorstore is None : 
        initialize_vectorstore()
    
    return _vectorstore.as_retriever(search_kwargs={'k' : 3})