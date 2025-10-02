from pdf_parser import extract_text_from_pdf
from embedder import create_vector_store, openai_key
from qa_engine import ask_question
from database import log_book, log_question

title = "Whispers of the Silk Road"
filename = "sample.pdf"

# Load PDF & embed
text = extract_text_from_pdf(filename)
store = create_vector_store(text)

# Book logging (should not re-insert now)
book_id = log_book(title, filename)

# Q&A logging (should not re-insert now)
question = "What is the main idea of this book?"
answer = ask_question(store, question, openai_key)
log_question(book_id, question, answer)

print("\n💬 Question:", question)
print("🤖 Answer:", answer)
