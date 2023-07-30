from dotenv import load_dotenv
from langchain import HuggingFaceHub,LLMChain
from langchain.prompts import PromptTemplate
import streamlit as st
st.header("Text Summarizer")
load_dotenv()
hub_llm=HuggingFaceHub(repo_id="facebook/bart-large-cnn")
prompt=PromptTemplate(input_variables=["question"],template="summarize the text: {question}")
hub_chain=LLMChain(prompt=prompt,llm=hub_llm,verbose=True)
#st.caption
a=st.text_input("type your text")
#x=st.chat_input("type your text")

if st.button("generate text"):
    st.text_area(hub_chain.run(a),max_chars=600)


    

#b=st.text(hub_chain.run(a))    
   


#st.title(x)
#st.chat_input("type your text")


