import os 
import streamlit as st
from PIL import Image
import google.generativeai as genai

# loading the invironment variables
from dotenv import load_dotenv
load_dotenv()

my_api_key = os.getenv("GOOGLE_API_KEY")

# configure the generative ai model with the retrieved api key
genai.configure(api_key = my_api_key)

# define out desired model
model = genai.GenerativeModel('gemini-1.5-flash')
def get_gemeni_response(user_quest, image):
    response = model.generate_content([user_quest, image])
    return response.text

st.set_page_config(page_title= 'GmeniVision', page_icon= '🤖')
st.title("Gemini PicAnalyzer Application ")
file  = st.file_uploader('choose an image...')
if file is not None:
    img = Image.open(file)
    st.image(img)
    width = 200
    st.subheader("Ask the model about the image")
with st.form(key = "input", clear_on_submit= True):
    user_quest = st.text_input("Your question about an image you uploaded ", placeholder = 'Type here...')
    btn = st.form_submit_button()
    if btn and user_quest:
        response = get_gemeni_response(user_quest, img)
        st.subheader("Answer: ")
        st.image(img)
        st.write(response)

    else:
        st.markdown('<div style="height: 300px;"></div>', unsafe_allow_html=True) 
        st.info('This bot uses the Google\'s Generative AI model, gemini-1.5-flash, developed by Kaletsidik. The model generates text based on the given input. The text generated by the model is not guaranteed to be accurate or helpful. If you need help with a specific issue, feel free to ask.')
        st.markdown('---')
        st.success("Made By Eyosias Mulugeta ©2024")
