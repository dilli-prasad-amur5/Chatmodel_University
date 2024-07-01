from langchain_community.embeddings import HuggingFaceEmbeddings, HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter 

DB_FAISS_PATH = 'FAISS_vectorstore_QA'

loader = PyPDFLoader('/home/jovyan/work/RAG/pdf_data/data.pdf')

documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)
texts = text_splitter.split_documents(documents)

embeddings = HuggingFaceBgeEmbeddings(model_name="BAAI/bge-large-en-v1.5",model_kwargs={'device': 'cuda'}, encode_kwargs = {'normalize_embeddings': True}) # encode kwargs set True to compute Cosine Similarity

db = FAISS.from_documents(texts, embeddings)
db.save_local(DB_FAISS_PATH)
