🧠 AI Agent Framework – Intel Unnati Submission
Overview
This project implements a modular AI Agent Framework using Python, FastAPI, and a local LLM (Ollama LLaMA-3).
The agent demonstrates a full Planner → Reasoner → Executor → Tools → Memory workflow:
1.	Planner – Breaks tasks into actionable steps
2.	Reasoner – Decides the next action using context & plan
3.	Executor – Runs tools like calculator on instructions
4.	Memory – Short-term & long-term memory support
5.	RAG – Retrieval-augmented generation pipeline for documents
The framework is extendable for real-world tasks, like PDF handling, OCR, or multi-agent collaboration.
________________________________________
📁 Folder Structure
ai-agent-framework-trifusion/
│
├── agents/
│   ├── base_agent.py         # Base agent class
│   ├── planner.py            # Planner agent
│   ├── reasoner.py           # Reasoner agent
│   ├── executor.py           # Executor agent
│
├── memory/
│   ├── short_term.py         # Short-term memory
│   ├── long_term.py          # Long-term vector memory
│
├── rag/
│   ├── document_loader.py    # Load text/PDF documents
│   ├── embedder.py           # Generate embeddings
│   ├── retriever.py          # Search/retrieve documents
│
├── tools/
│   ├── calculator.py         # Calculator tool
├── llm/
│   ├── llm_client.py         # LLM integration (Ollama LLaMA-3)
│
├── api/
│   ├── main.py               # FastAPI entrypoint
│
├── data/
│   ├── docs/                 # Sample documents for RAG
│
└── requirements.txt          # Project dependencies
________________________________________
🛠 Setup Instructions
1️⃣ Clone and Setup Environment
git clone https://github.com/yourusername/ai-agent-framework-trifusion.git
cd ai-agent-framework-trifusion

# Create virtual environment
python -m venv venv
# Activate virtual environment
venv\Scripts\activate     # Windows
# or
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
pip install langchain-ollama
2️⃣ Pull Ollama LLaMA-3 Model (optional, if using local LLM)
ollama pull llama3
________________________________________
🧠 LLM Integration (llm/llm_client.py)
Supports Ollama LLaMA-3 for local LLM inference.
________________________________________
🗂 Core Agents
1️⃣ Planner (agents/planner.py)
2️⃣ Reasoner (agents/reasoner.py)
3️⃣ Executor (agents/executor.py)
________________________________________
🧮 Calculator Tool (tools/calculator.py)
________________________________________
🧠 Memory System
Short-Term Memory (memory/short_term.py)
Long-Term Memory (memory/long_term.py)
📚 RAG Pipeline
•	Document Loader: rag/document_loader.py
•	Embedder: rag/embedder.py
•	Retriever: rag/retriever.py
Used for retrieval-augmented generation from documents.
________________________________________
🌐 FastAPI API (api/main.py)
________________________________________
Run the server:
python -m uvicorn api.main:app --reload
Open browser: http://127.0.0.1:8000/docs
•	Test /agent endpoint
•	Enter JSON:
{"query": "Calculate 24 * 5"}
•	You should see:
{
  "plan": "...",
  "action": "...",
  "result": 120
}
________________________________________
🎯 Key Features
•	Planner → Reasoner → Executor modular pipeline
•	Tool execution (Calculator implemented, easy to extend)
•	Short-term & Long-term memory
•	RAG integration for document retrieval
•	Ollama LLaMA-3 local LLM support
•	FastAPI endpoint for real-world deployment
________________________________________
🔹 Next Extensions 
•	Multi-agent collaboration
•	PDF/Document ingestion
•	Integration with OCR / Digital Twins
•	Intel OpenVINO optimization for LLM
________________________________________
🔹Credits
•	Initial agent prompt patterns and architectural guidance assisted by ChatGPT
•	Full implementation, integration, debugging, and customization – Team TriFusion.
Note: This is developed by team TriFusion as a part of Intel Unnati Training for 
Problem Statement: Build your own AI Agent Framework

Authors: Donthi Nishitha | Subraveti Deepthi | Pebbeti Navya Sri
