import streamlit as st

st.set_page_config(page_title='Chat with Websites', page_icon='🤖')
st.title('Chat with Websites')

with st.sidebar:
    st.header('Settings')
    website_url = st.text_input('Website URL')

st.chat_input('Type a message')

with st.chat_message('AI'):
    st.write('Hello, I am an AI!')

with st.chat_message('Human'):
    st.write('Hello, I am a human! I want to know more about Langchain!')
