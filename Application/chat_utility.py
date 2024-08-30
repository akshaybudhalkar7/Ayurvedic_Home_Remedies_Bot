import os
import logging
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

working_dir = os.path.dirname(os.path.abspath(__file__))
DB_FAISS_PATH = "Application/vectorstore/db_faiss"


llm = Ollama(
    model="gemma2:2b",
    temperature=0
)

def get_answer(query):
    logging.info("Starting get_answer function")

    embeddings = HuggingFaceEmbeddings()

    knowledge_base = FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)

    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=knowledge_base.as_retriever()
    )
    logging.info("QA chain created")

    response = qa_chain.invoke({"query": query})
    logging.info(f"Response received: {response['result']}")

    return response["result"]
