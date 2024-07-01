import streamlit as st

st.write("### Instructions for Using the Chatbot ###")

with st.expander("Instructions for Using this Chatbot effectively"):
    st.markdown("""
        - **Be Specific:** Provide clear and detailed information in your questions.
    
        - **Use Full Sentences:** Instead of single words or short phrases, use full sentences to convey your query. This helps the chatbot understand the nuance of your request.
    
        - **Limit One Question per Submission:** If you have multiple questions, ask them one at a time to get focused answers for each.
    
        - **Rephrase Ambiguous Queries:** If you don't get the expected answer, try rephrasing your question to eliminate any ambiguity.
    
        - **Avoid Slang and Abbreviations:** Use standard language and avoid using slang terms or too many abbreviations which the chatbot may not understand.
    
        - **Check Your Spelling:** Misspelled words can confuse the chatbot, so double-check your text before submitting.
    
        - **Keep Personal Information Private:** Don't share personal or sensitive information. The chatbot is designed to provide information and answer questions based on the content it has been trained on.
    
        - **Be Patient:** Sometimes, generating a response may take a moment. Please wait for the chatbot to reply before sending another query.
        
        - **Related questions:** The chatbot can sometimes provide you question and answers data in output. This is because it has been trained on some question answer pairs and it can give this data for you.
    
    """)