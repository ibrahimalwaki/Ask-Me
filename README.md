# Ask Me

A web app that lets you have a conversation with any PDF. Upload a book, lecture notes, or any document, and Ask Me builds a searchable index on the spot — then answers your questions using semantic retrieval backed by OpenAI.

## What it does

- Upload one or more PDF files through the sidebar
- Each document gets chunked, embedded, and stored in a FAISS vector index
- Ask any question in natural language and get answers grounded in the actual text
- Every book and question is logged to a local SQLite database for session history
- Delete a book to remove it from the session

## Tech stack

- **Streamlit** — UI and session management
- **LangChain** — document loading, chunking, and QA chain orchestration
- **FAISS** — in-memory vector search
- **OpenAI** — text embeddings and language model for answering
- **pdfplumber / pdfminer** — PDF text extraction
- **SQLAlchemy + SQLite** — lightweight persistence for history

## Setup

1. Clone the repo and create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Create a `.env` file at the project root:
   ```
   OPENAI_API_KEY=your_key_here
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

## Project structure

```
app.py            — Streamlit entry point and UI logic
pdf_parser.py     — Text extraction from uploaded PDFs
embedder.py       — Chunking and FAISS vector store creation
qa_engine.py      — LangChain retrieval-QA chain
database.py       — SQLite logging for books and questions
```

## Notes

- The vector index lives in memory per session; uploading the same PDF again re-indexes it.
- Keep PDFs under ~200 pages for reasonable response times with the free OpenAI tier.
- The `.env` file is gitignored — never commit API keys directly to source.
