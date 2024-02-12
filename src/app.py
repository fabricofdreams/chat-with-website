import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def get_response(user_input):
    return "I don't know."


def get_vectorstore_from_url(url):
    # Content in document format
    loader = WebBaseLoader(url)
    document = loader.load()

    # Split document into chunks
    text_splitter = RecursiveCharacterTextSplitter()
    document_chunks = text_splitter.split_documents(document)
    return document_chunks


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

if website_url is None or website_url == '':
    st.info('Please enter a website URL.')
else:
    document_chunks = get_vectorstore_from_url(website_url)
    with st.sidebar:
        st.header('Website')
        st.write(document_chunks)

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
