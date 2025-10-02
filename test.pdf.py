from pdf_parser import extract_text_from_pdf

text = extract_text_from_pdf("sample.pdf")  # use your actual PDF filename here
print(text[:1000])
