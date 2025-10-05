🩺 MediAid: AI Medical Assistant

🎯 Objective
Built an enterprise-grade, LangGraph-powered Multi-Agent Medical AI Assistant capable of delivering compassionate, doctor-like responses with real-time reasoning and dynamic fallback logic. The system integrates Planner, LLM, RAG Retriever, Wikipedia, DuckDuckGo, Executor, and Explanation Agents in a stateful orchestration pipeline, enabling context-aware decision-making and intelligent tool routing. Implemented RAG using medical PDFs with PyPDFLoader, HuggingFaceEmbeddings, and Chroma for fast, accurate retrieval, and leveraged ChatGroq (GPT-OSS-120B) for empathetic, natural-language responses. Designed with short-term memory, multi-stage planning, and adaptive fallback mechanisms, ensuring robust, production-ready performance suitable for real-world medical consultation use cases.

🔗 Live Demo
You can interact with the live AI-powered medical assistant here: 👉 https://medigenius.onrender.com/

🌍 Real-World Use Cases
Rural Health Access Providing preliminary medical advice in rural or underserved areas where certified doctors may not be immediately available.

Mental Health First Aid Offering supportive conversations for users dealing with stress, anxiety, or medical confusion.

Patient Pre-screening Collecting and analyzing symptoms before a user visits a doctor, reducing clinical workload.

Home Care Guidance Guiding patients and caregivers on medication usage, symptoms, or recovery advice.

Educational Assistant Helping medical students or patients understand medical topics in simpler language.

🚀 Features
🤖 Doctor-like medical assistant with empathetic, patient-friendly communication
🧠 LLM-powered primary response engine using ChatGroq (GPT-OSS-120B)
📚 RAG (Retrieval-Augmented Generation) from indexed medical PDFs using PyPDFLoader + HuggingFace Embeddings + ChromaDB
🗺️ Planner Agent for intelligent tool selection and decision-making
🌐 Wikipedia fallback for general medical knowledge retrieval
🔎 DuckDuckGo fallback for up-to-date or rare medical information
🗂️ Vector database (ChromaDB) with persistent cosine-similarity search
🧩 Multi-agent orchestration via LangGraph with Planner, Retriever, Executor, and Explanation agents
💬 Short-term conversation memory for context-aware responses
🔄 Dynamic fallback chain ensuring robust answers even in edge cases
📜 Conversation logging for traceability and debugging
⚡ Production-ready modular design for integration into healthcare chat systems
🔒 Rest API for integration with other systems
🐳 Dockerized deployment for consistent environment and easy scaling
🌐 Flask backend with custom HTML, CSS, and JavaScript frontend for smooth UX
🔁 CI/CD pipeline integration for automated testing and deployment
🗂️ Technical Stack
Category	Technology/Resource
Core Framework	LangChain, LangGraph
Multi-Agent Orchestration	Planner Agent, LLM Agent, Retriever Agent, Wikipedia Agent, DuckDuckGo Agent, Executor Agent, Explanation Agent
LLM Provider	Groq (GPT-OSS-120B)
Embeddings Model	HuggingFace (sentence-transformers/all-MiniLM-L6-v2)
Vector Database	ChromaDB (cosine similarity search)
Document Processing	PyPDFLoader (PDF), RecursiveCharacterTextSplitter
Search Tools	Wikipedia API, DuckDuckGo Search
Conversation Flow	State Machine (LangGraph) with multi-stage fallback logic
Medical Knowledge Base	Domain-specific medical PDFs + Wikipedia medical content
Backend	Flask (REST API + application logic)
Frontend	Custom HTML, CSS, JavaScript UI
Deployment	Docker (containerized), Local Development, Production-ready build
CI/CD	GitHub Actions (automated testing & deployment)
Environment Management	python-dotenv (environment variables)
Logging & Monitoring	Console + file logging with full traceback
Hosting	Render
🗂️ Folder Structure
MediGenius/
├── .github/
│   └── workflows/
│       └── main.yml
│
├── agents/
│   ├── __init__.py
│   ├── duckduckgo_agent.py
│   ├── executor_agent.py
│   ├── explanation_agent.py
│   ├── llm_agent.py
│   ├── memory_agent.py
│   ├── planner_agent.py
│   ├── retriever_agent.py
│   └── wikipedia_agent.py
│ 
├── core/
│   ├── __init__.py
│   ├── langgraph_workflow.py
│   └── state.py
│
├── data/
│   └── medical_book.pdf
│
├──── medical_db/
│   └── chroma.sqlite3
│
├── notebook/
│   └── experiment.ipynb
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
│
├── templates/
│   ├── base.html
│   └── index.html
│
├── tests/
│   └── test_app.py
│
├── tools/
│   ├── __init__.py
│   ├── llm_client.py
│   ├── pdf_loader.py
│   └── vector_store.py
│
├── .gitignore
├── api.py
├── app.png
├── app.py
├── demo.mp4
├── Dockerfile
├── LICENSE
├── main.py
├── README.md
├── render.yaml
├── requirements.txt
└── setup.py
🧱 Project Architecture

API Endpoints
Base URL
http://localhost:8000

Endpoints
POST /chat
Process a medical question and return AI response

Request:

POST /chat HTTP/1.1
Content-Type: application/json
Host: localhost:8000

{
  "message": "What are diabetes symptoms?",
  "conversation_id": "optional_existing_id"
}
Parameters:

message (required): The medical question to process
conversation_id (optional): Existing conversation ID for context
Response:

{
  "response": "Diabetes symptoms include increased thirst, frequent urination...",
  "timestamp": "12:30",
  "conversation_id": "20240615123045"
}
Status Codes:

200: Successful response
400: Invalid request (missing message)
500: Internal server error
Example Usage
Starting a new conversation:
POST /chat
{
  "message": "What causes migraines?"
}
Response:

{
  "response": "Migraines may be caused by genetic factors, environmental triggers...",
  "timestamp": "14:25",
  "conversation_id": "20240615142500"
}
🧭 Future Improvements
🎙️ Add voice input/output
🖼️ Add image upload for reports or prescriptions
🧬 Integrate with real-time medical APIs (e.g., WebMD)
🔐 Add user authentication & role-based chat memory
👨‍💻 Developed By
Mahamudul Hasan
📧 Email: hasansayeed791@gmail.com
💬 WhatsApp: +8801690103839


📌 License
MIT License. Free to use with credit.
