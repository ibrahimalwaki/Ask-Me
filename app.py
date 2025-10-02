# app.py

import streamlit as st
import os
from pdf_parser import extract_text_from_pdf
from embedder import create_vector_store, openai_key
from qa_engine import ask_question
from database import log_book, log_question, get_book_history

# Page settings
st.set_page_config(page_title="Ask My Book", layout="wide")
st.title("📘 Ask My Book")
st.markdown("Upload multiple books and chat with each one.")

# Session state
if "books" not in st.session_state:
    st.session_state.books = {}

# Upload PDF
st.sidebar.header("📤 Upload New Book")
pdf_file = st.sidebar.file_uploader("Choose a PDF", type=["pdf"])

if pdf_file:
    with st.spinner("📚 Processing uploaded book..."):
        title = pdf_file.name
        file_path = f"temp_{title}"

        with open(file_path, "wb") as f:
            f.write(pdf_file.read())

        text = extract_text_from_pdf(file_path)
        vector_store = create_vector_store(text)
        book_id = log_book(title, file_path)

        st.session_state.books[title] = {
            "id": book_id,
            "path": file_path,
            "store": vector_store
        }

        st.success(f"✅ '{title}' added and ready to chat.")

# If books exist
if st.session_state.books:
    st.sidebar.header("📚 Select Book")
    selected_book = st.sidebar.selectbox(
        "Choose a book to chat with:",
        list(st.session_state.books.keys())
    )

    # Option to delete
    if st.sidebar.button("🗑️ Delete This Book"):
        file_to_delete = st.session_state.books[selected_book]["path"]
        try:
            os.remove(file_to_delete)
        except Exception as e:
            st.sidebar.warning(f"⚠️ Could not delete file: {e}")
        del st.session_state.books[selected_book]
        st.sidebar.success(f"'{selected_book}' deleted.")
        st.rerun()

    # Proceed if selected
    else:
        active = st.session_state.books[selected_book]
        book_id = active["id"]
        vector_store = active["store"]

        # History
        st.sidebar.subheader("🕘 History")
        history = get_book_history(book_id)
        if not history:
            st.sidebar.info("No questions yet.")
        else:
            for idx, (q, a, t) in enumerate(history):
                with st.sidebar.expander(f"Q{idx+1}: {q[:50]}...", expanded=False):
                    st.sidebar.markdown(f"**Q:** {q}")
                    st.sidebar.markdown(f"**A:** {a}")
                    st.sidebar.caption(f"🕒 {t}")

        # Ask question
        st.subheader(f"📖: {selected_book}")
        question = st.text_input("💬 Ask a question:")
        if question:
            with st.spinner("🤖 Generating answer..."):
                answer = ask_question(vector_store, question, openai_key)
                log_question(book_id, question, answer)
                st.markdown(f"**🤖 Answer:** {answer}")
else:
    st.info("Upload a book from the sidebar to begin.")


# command that you should runs in the terminal is streamlit run app.py
