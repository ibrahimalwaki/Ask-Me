from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import os

# ✅ Load .env using ABSOLUTE path
load_dotenv(dotenv_path="/Users/alwaki/ask-my-book/.env")  # ← replace with your actual path

# ✅ Confirm the key is loaded
openai_key = "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"
print("OpenAI Key Loaded:", bool(openai_key))

def create_vector_store(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", ".", "!", "?", ",", " ", ""]
    )
    chunks = splitter.split_text(text)

    embeddings = OpenAIEmbeddings(openai_api_key=openai_key)
    store = FAISS.from_texts(chunks, embeddings)
    return store
if __name__ == "__main__":
    print("Module loaded successfully!")
