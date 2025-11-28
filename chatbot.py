import streamlit as st
import google.generativeai as genai
import pyttsx3 as p

key = "AIzaSyD........AXo"
# Replace with your actual API key

genai.configure(api_key = key)
model = genai.GenerativeModel("gemini-2.5-flash")



st.title("Jarvis AI chatbotbot")
st.text("Welcome  Sir")
v1 = st.header(" I am Jarvis Aditya's sir assistant")


st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9XLivsO-xxDub9a0aFnA97WyDCLAcpJvJoZ9WMUuLCRt3PqWDjBzdh-GBsSfxQuMn8-o&usqp=CAU")
name = st.text_input("ENTER your name : ")
v2 = st.write("welcome",name, "I am jarvis how could I help you")



user = st.text_input("ENTER  What you want from jarvis  : ")
if st.button ("Generate the response "):
    Jarvis = model.generate_content(user)
    response = Jarvis.text
    v3 = st.write("jarvis : ",response)
    speaker = p.init()
    speaker.say(response)
    speaker.runAndWait()
    del speaker

	


