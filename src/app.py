import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever


load_dotenv()


def get_response(user_input):
    return "I don't know."


def get_vectorstore_from_url(url):
    # Content in document format
    loader = WebBaseLoader(url)
    document = loader.load()

    # Split document into chunks
    text_splitter = RecursiveCharacterTextSplitter()
    document_chunks = text_splitter.split_documents(document)

    # Create a vectorstore from the chunks
    vectorstore = Chroma.from_documents(document_chunks, OpenAIEmbeddings())

    return vectorstore


def get_context_retriever_chain(vectorstore):
    llm = ChatOpenAI()

    retriever = vectorstore.as_retriever()

    prompt = ChatPromptTemplate.from_messages([
        MessagesPlaceholder(variable_name='chat_history'),
        ("user", "{input}"),
        ("user", "Given the above conversation, generate a search query to look up in order to get information relevant to the conversation."),
    ])

    retriever_chain = create_history_aware_retriever(llm, retriever, prompt)

    return retriever_chain


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
    vectorstore = get_vectorstore_from_url(website_url)

    retriever_chain = get_context_retriever_chain(vectorstore)

    # User input
    user_query = st.chat_input('Type your message here...')
    if user_query is not None and user_query != '':
        response = get_response(user_query)
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        st.session_state.chat_history.append(AIMessage(content=response))

        retrieved_documents = retriever_chain.invoke({
            'chat_history': st.session_state.chat_history,
            'input': user_query
        })
        st.write(retrieved_documents)

    # Conversation
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message('AI'):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message('Human'):
                st.write(message.content)
