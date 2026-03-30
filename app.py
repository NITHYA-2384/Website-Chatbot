import streamlit as st
try:
    import speech_recognition as sr
    import pyttsx3
    voice_enabled = True
except:
    voice_enabled = False
import time

from backend import create_vectorstore, get_answer
from text_splitter import split_text

with open("data/website_data.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunks = split_text(text)
db = create_vectorstore(chunks)

st.set_page_config(page_title="Website Chatbot", layout="wide")
st.title("Website Chatbot with Voice")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "engine" not in st.session_state:
    st.session_state.engine = pyttsx3.init()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


if voice_enabled and st.button("🛑 Stop Voice"):
    st.session_state.engine.stop()

if voice_enabled and st.button("🎤 Speak"):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("Listening...")
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio)

        
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)

       
        response = get_answer(db, user_input)

      
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            for word in response.split():
                full_response += word + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + "▌")

            message_placeholder.markdown(full_response)

        st.session_state.messages.append({"role": "assistant", "content": response})

    
        engine = st.session_state.engine
        engine.stop()
        engine.say(response)
        engine.runAndWait()

    except:
        st.error("Could not understand audio")


user_input = st.chat_input("Ask something...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

  
    response = get_answer(db, user_input)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        for word in response.split():
            full_response += word + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")

        message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": response})

    engine = st.session_state.engine
    engine.stop()
    engine.say(response)
    engine.runAndWait()
