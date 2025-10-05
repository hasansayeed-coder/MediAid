from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

_llm = None

def get_llm() :
    global _llm
    if _llm is None : 
        _llm = ChatGroq(
            model_name = "" , 
            temperature = 0.3 , 
            max_tokens=2048
        )
    return _llm