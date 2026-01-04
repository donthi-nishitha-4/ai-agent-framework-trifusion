from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from rag.document_loader import load_docs

class Retriever:
    def __init__(self):
        docs = load_docs()
        self.db = FAISS.from_texts(docs, HuggingFaceEmbeddings())

    def fetch(self, query):
        return self.db.similarity_search(query, k=3)
