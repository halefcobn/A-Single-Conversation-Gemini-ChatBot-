from dotenv import load_dotenv
load_dotenv() # load env variable

import streamlit as st
import os
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel("gemini-pro")
#gemini pro model
def get_response(question):
    response = model.generate_content(question)
    return response.text

#Streamlit Config
st.set_page_config(page_title='Gemini Pro Demo App')

st.header('Gemini Pro LLM Application')

input = st.text_input("Input: ", key="input") 
sumbit = st.button("Ask a Question")


#when question is submitted

if sumbit:
    response = get_response(input)
    st.subheader("The Response is")
    st.write(response)
    
    