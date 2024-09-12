import voyageai

vo = voyageai.Client(api_key)

EMD_MODEL_SIZE = 1024
COLLECTION_NAME = "voyage-2-law"
model_rag="voyage-law-2"
db_create = False # Set to true if you want to create a vector store, false if it is already created

#from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma
from langchain_voyageai import VoyageAIEmbeddings
from langchain.schema import Document

embeddings = VoyageAIEmbeddings(model=model_rag,
                              voyage_api_key="",
                              show_progress_bar=True)

db_path = f'/content/drive/MyDrive/NLLP/db/{provider}_t&c'

if db_create == True:
  #documents = []

  #for chunk in chunks:
    #documents.append("\n".join(page))


  # Assuming 'pages' is your list of strings
  documents = [Document(page_content=page) for page in chunks]
  vectorstore = Chroma.from_documents(
      collection_name = COLLECTION_NAME,
      persist_directory = db_path,
      documents = documents,
      embedding = embeddings,
      collection_metadata={"hnsw:space": "cosine"})
