from pdf_parser import extract_text_from_pdf
from embedder import create_vector_store

text = extract_text_from_pdf("sample.pdf")
store = create_vector_store(text)

print(" Vector store created with embedded book chunks!")

