import streamlit as st
from streamlit_chat import message
from streamlit_feedback import streamlit_feedback

from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers, HuggingFaceHub

from langchain.retrievers import ParentDocumentRetriever
from langchain.retrievers.merger_retriever import MergerRetriever
from langchain.storage import InMemoryStore

from langchain_community.embeddings import HuggingFaceEmbeddings, HuggingFaceBgeEmbeddings
from langchain_community.llms import LlamaCpp
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS,Chroma
from langchain.memory import ConversationBufferMemory
from langchain_community.document_loaders import PyPDFLoader

from dataclasses import dataclass
from typing import Literal

import os
import tempfile
import base64


def custom_prompt():
    custom_prompt_template = """Use the following pieces of information to answer the user's question about TH Rosenheim University.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.
    
    Context: {context}
    Question: {question}
    
    Only return the helpful answer below and nothing else.
    Helpful answer:
    """
    prompt = PromptTemplate(template=custom_prompt_template,
                                input_variables=['context', 'question'])
    return prompt

def files_retriever(embeddings):
    DB_FAISS = 'FAISS_vectorstore_files'
    db = FAISS.load_local(DB_FAISS, embeddings)
    retriever_files = db.as_retriever(search_type = 'similarity', search_kwargs = {'k':2})
    return retriever_files

def QA_retriever(embeddings):
    DB_FAISS_QA = 'FAISS_vectorstore_QA'
    db_qa = FAISS.load_local(DB_FAISS_QA, embeddings)
    retriever_QA= db_qa.as_retriever(search_type = 'similarity', search_kwargs = {'k':3})
    return retriever_QA

def merge_retriever(retriever_files, retriever_QA):
    
    merge_retriever = MergerRetriever(retrievers = [retriever_files, retriever_QA])
    
    return merge_retriever

def llm_model():
    HF_TOKEN = "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"
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = HF_TOKEN
    llm_model = HuggingFaceHub(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",
        model_kwargs={"temperature": 0.3,"max_new_tokens":512})
    return llm_model

#query = "tell me about application process at Rosenheim university of Applied sciences:"
#result = qa_chain({"query": query}) #({'query': query})

def initialize_session_state():
    if 'history' not in st.session_state:
        st.session_state['history'] = []

    if 'history1' not in st.session_state:
        st.session_state['history1'] = []

    if 'generated' not in st.session_state:
        st.session_state['generated'] = ["Hello! Ask me anything about TH Rosenheim University🤗"]

    if 'past' not in st.session_state:
        st.session_state['past'] = ["Hey! 👋"]

    if 'user_input' not in st.session_state:
        st.session_state.user_input = ""
        
    if 'responses' not in st.session_state:
        st.session_state['responses'] = []

def conversation_chat(query, chain, history):
    result = chain({"question": query, "chat_history": history})
    history.append((query, result["answer"]))
    return result["answer"]


@dataclass
class Message:
    """Class for keeping track of a chat message."""
    origin: Literal["human", "ai"]
    message: str

def load_css():
    with open("static/styles.css", "r") as f:
        css = f"<style>{f.read()}</style>"
        st.markdown(css, unsafe_allow_html=True)
        
def convert_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

def page_config():
    conf = st.set_page_config(
        page_title="TH Rosenheim University Bot",
        page_icon="🏫",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://www.extremelycoolapp.com/help',
            'Report a bug': "mailto:dilliprasad.amur@stud.th-rosenheim.de",
            'About': "This chatbot is designed as a part of my Masters Thesis and it helps to assist users about TH Rosenheim University. The data and information for this chatbot have been sourced directly from the [TH Rosenheim University website](https://www.th-rosenheim.de). All content and information provided by this chatbot are the property of TH Rosenheim University. Copyright laws protect the intellectual property and information pertaining to the university's courses, research, and other academic resources. **Note**: This chatbot is an independent project and is not officially endorsed by TH Rosenheim University."
        })
    return conf

def add_new_chat_button():
    if st.sidebar.button('Clear Chat'):
        st.session_state['history'] = []
        st.session_state['history1'] = []
        st.session_state['generated'] = ["Hello! Ask me anything about TH Rosenheim University🤗"]
        st.session_state['past'] = ["Hey! 👋"]
        st.session_state['responses'] = []
        
        st.experimental_rerun()

def handle_feedback():  
    #st.write(st.session_state.fb_k)
    st.toast("✔️ Feedback received!")



def display_chat_history(chain):
    chat_placeholder = st.container()
    container = st.container()

    # Use a form for the input and submit button
    with container:
        with st.form(key='chat_form', clear_on_submit=True):
            user_input = st.text_input("Enter your question", placeholder="Query about TH Rosenheim", key='input')
            submit_button = st.form_submit_button(label='Submit')
    
        if submit_button and user_input:
            with st.spinner('Generating response...'):
                
                output = conversation_chat(user_input, chain, st.session_state['history'])
                st.session_state.history1.append(Message("human", user_input))
                st.session_state.history1.append(Message("ai", output))
        
        with chat_placeholder:
            ai_icon_base64 = convert_image_to_base64("static/ai_icon.png")
            user_icon_base64 = convert_image_to_base64("static/user_icon.png")
            
            for chat in st.session_state.history1:
                div = f"""
                <div class="chat-row {'' if chat.origin == 'ai' else 'row-reverse'}">
                    <img class="chat-icon" src="data:image/png;base64,{ai_icon_base64 if chat.origin == 'ai' else user_icon_base64}"
                         width=32 height=32>
                    <div class="chat-bubble {'ai-bubble' if chat.origin == 'ai' else 'human-bubble'}">
                        &#8203;{chat.message}
                    </div>
                </div>
                """
                st.markdown(div, unsafe_allow_html=True)

            with st.form('feedback_form'):
                streamlit_feedback(feedback_type="thumbs",
                                    optional_text_label="[Optional] Please provide an explanation", 
                                    align="flex-start", 
                                    key='fb_k')
                st.form_submit_button('Save feedback', on_click=handle_feedback)
            
            for _ in range(3):
                st.markdown("")
    #st.experimental_rerun()

def main():
    # Initialize session state
    page_config()
    load_css()
    initialize_session_state()
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("THRosenheim.png")
    #st.image("THRosenheim.png")
    st.title('Welcome to TH Rosenheim Chatbot')

    text = "This application is designed to provide you with quick response to your queries about the university. TH Rosenheim University chatbot is here to assist you by providing the information available on university website in quick time and can provide details about courses, admissions, facilities and all university related information."

    custom_html = f"""
    <div style="font-size: 18px;">  <!-- Change font family as needed -->
        {text}
    </div>
"""
    st.markdown(custom_html, unsafe_allow_html=True)
    
    st.sidebar.title("") 

    add_new_chat_button()
    
    
    llm = llm_model()
    
    embeddings = HuggingFaceBgeEmbeddings(model_name="BAAI/bge-large-en-v1.5",
                                       model_kwargs={'device': 'cuda'}, encode_kwargs = {'normalize_embeddings': True})

    retriever1 = files_retriever(embeddings)  
    retriever2 = QA_retriever(embeddings)
    retriever = merge_retriever(retriever1, retriever2) 
    
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    prompt = custom_prompt()
    qa_chain = ConversationalRetrievalChain.from_llm(llm=llm, chain_type='stuff',
                                                 retriever=retriever,
                                                 memory=memory,
                                                    combine_docs_chain_kwargs={"prompt": prompt})     
    #chat_placeholder.empty()    
    display_chat_history(qa_chain)

if __name__ == "__main__":
    main()

