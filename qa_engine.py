# qa_engine.py

from langchain_community.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

def ask_question(vector_store, query, api_key):
    llm = OpenAI(openai_api_key=api_key, temperature=0)
    retriever = vector_store.as_retriever()
    docs = retriever.get_relevant_documents(query)

    chain = load_qa_chain(llm, chain_type="stuff")
    response = chain.run(input_documents=docs, question=query)
    return response
