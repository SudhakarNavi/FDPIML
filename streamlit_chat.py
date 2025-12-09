import streamlit as st
import requests

st.title("🎓 Student Support Bot (Rasa)")
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

def send(msg):
    st.session_state['messages'].append(("You", msg))
    r=requests.post("http://localhost:5005/webhooks/rest/webhook",
                    json={"sender":"user","message":msg})
    if r.ok:
        for m in r.json():
            st.session_state['messages'].append(("Bot", m.get("text","")))
    else:
        st.session_state['messages'].append(("Bot","Error."))

inp = st.text_input("You:")
if st.button("Send"):
    send(inp)

for who,msg in st.session_state['messages']:
    st.write(f"**{who}:** {msg}")
