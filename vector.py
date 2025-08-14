# transform the csv file to database for the llm 
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd


df = pd.read_csv("customers-10000.csv")


# initialize the embedding model that we pulled earluer via ollama
embeddings=OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chrome_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []
    
    for i, row in df.iterrows():
        document = Document(
            page_content=(
                f"Customer: {row['First Name']} {row['Last Name']} from {row['Company']} in {row['City']}, {row['Country']}. "
                f"Contact: {row['Email']} | Phone: {row['Phone 1']}. "
                f"Website: {row['Website']}"
            ),
            metadata={
                "customer_id": row["Customer Id"],
                "company": row["Company"],
                "city": row["City"],
                "country": row["Country"],
                "phone_2": row["Phone 2"],
                "subscription_date": row["Subscription Date"]
            }
        )
            
        ids.append(str(i))
        documents.append(document)

vector_store = Chroma(
    collection_name = "customers_informations",
    persist_directory=db_location,
    embedding_function=embeddings
)
if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)
    

# make this vector store usuable by the llm
# the k:5 is to specify how many documents we want to pass to the llm
retriever = vector_store.as_retriever(
    search_kwargs={"k":5}
)
