from langchain_community.embeddings import HuggingFaceEmbeddings, HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter 

DB_FAISS_PATH = 'FAISS_vectorstore_files'

loader = PyPDFLoader('/home/jovyan/work/RAG/pdf_data/files.pdf')

documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
texts = text_splitter.split_documents(documents)

embeddings = HuggingFaceBgeEmbeddings(model_name="BAAI/bge-large-en-v1.5",model_kwargs={'device': 'cuda'}, encode_kwargs = {'normalize_embeddings': True}) # encode kwargs set True to compute Cosine Similarity

db = FAISS.from_documents(texts, embeddings)
db.save_local(DB_FAISS_PATH)
