from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_pdf_documents(file_path : str) : 
    loader = PyPDFLoader(file_path)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size = 512 , 
        xhunk_overlap = 128 , 
        seperators = ["\n\n" , ". " , "\n" , " "]
    )

    return text_splitter.split_documents(docs)