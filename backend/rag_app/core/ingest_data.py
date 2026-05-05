import pandas as pd
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config.settings import DATA1_DIR_RAG_BASE, DATA2_DIR_RAG_BASE, CHUNK_SIZE, CHUNK_OVERLAP, LENGTH_FUNCTION

########################################################################################################################
### Read your CSV files, chunk them, and save them to the Chroma vector database. You only run this when you add new data.
########################################################################################################################

def build_database():
    print("Loading data...")
    df1 = pd.read_csv(DATA1_DIR_RAG_BASE)
    df2 = pd.read_csv(DATA2_DIR_RAG_BASE)

    documents =[]

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE, 
        chunk_overlap=CHUNK_OVERLAP,
        length_function=LENGTH_FUNCTION,
        separators=["\n\n", "\n", " ", ""] 
    )

    print("Processing Data 1...")
    for _, row in df1.iterrows():
        question = str(row['Context'])
        full_answer = str(row['Response'])
        answer_chunks = text_splitter.split_text(full_answer)
        
        for chunk in answer_chunks:
            text = f"User Issue: {question}\n\nCounselor Response (Part): {chunk}"
            documents.append(Document(page_content=text, metadata={"source": "data1"}))

    print("Processing Data 2...")
    for _, row in df2.iterrows():
        text = f"User Issue: {str(row['question'])}\n\nCounselor Response: {str(row['response_j'])}"
        documents.append(Document(page_content=text, metadata={"source": "data2"}))

    print(f"Created {len(documents)} document chunks.")
    print("Creating local vector database...")

    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    # Build and persist the database
    Chroma.from_documents(
        documents=documents, 
        embedding=embeddings, 
        persist_directory="./local_db"
    )
    print("Database successfully built and saved to './local_db'")

if __name__ == "__main__":
    build_database()