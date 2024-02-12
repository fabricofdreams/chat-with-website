import streamlit as st


def get_response(user_input):
    return "I don't know."


# App configuration
st.set_page_config(page_title='Chat with Websites', page_icon='🤖')
st.title('Chat with Websites')

# Sidebar
with st.sidebar:
    st.header('Settings')
    website_url = st.text_input('Website URL')

# User input
user_query = st.chat_input('Type a message')

if user_query is not None and user_query != '':
    response = get_response(user_query)
    with st.chat_message('Human'):
        st.write(user_query)
    with st.chat_message('AI'):
        st.write(response)
