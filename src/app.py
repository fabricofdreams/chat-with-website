import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage


def get_response(user_input):
    return "I don't know."


# App configuration
st.set_page_config(page_title='Chat with Websites', page_icon='🤖')
st.title('Chat with Websites')

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content='Hi! How can I help you?')
    ]

# Sidebar
with st.sidebar:
    st.header('Settings')
    website_url = st.text_input('Website URL')

# User input
user_query = st.chat_input('Type a message')

if user_query is not None and user_query != '':
    response = get_response(user_query)
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    st.session_state.chat_history.append(AIMessage(content=response))


# Conversation
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message('AI'):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message('Human'):
            st.write(message.content)
