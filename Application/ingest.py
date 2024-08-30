from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

faiss_path = "vectorstore/db_faiss"

def create_vector_store():
    embeddings = HuggingFaceEmbeddings()
    data_path = "source_data/"
    loader = DirectoryLoader(data_path, glob="*.pdf",loader_cls = PyPDFLoader)
    documents = loader.load()
    logging.info(f"Loaded {len(documents)} documents")

    # Create text chunks
    text_spliter = CharacterTextSplitter(separator="/n",
                                         chunk_size=1000,
                                         chunk_overlap=200)
    text_chunks = text_spliter.split_documents(documents)
    logging.info(f"Text chunks created: {len(text_chunks)} chunks")

    # Vector embeddings from text chunks
    knowledge_base = FAISS.from_documents(text_chunks, embeddings)
    logging.info("Knowledge base created with FAISS")

    logging.info(f"Saving FAISS vector store to {faiss_path}")
    knowledge_base.save_local(faiss_path)

create_vector_store()
