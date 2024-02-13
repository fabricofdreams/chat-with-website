# Chat with Websites

Chat with Websites is a web application that enables users to engage in conversational interactions with websites using an AI-powered chatbot.

## Features

- **Conversational Interaction**: Users can communicate with websites in a conversational manner, simulating human-like interactions.
  
- **Website Content Analysis**: The application fetches content from the specified website URL and processes it to create a vector store, enabling better understanding of the website context during conversations.
  
- **Conversational RAG Model**: Utilizes a Conversational RAG (Retrieval Augmented Generator) model to generate responses based on user queries and contextual information derived from the website content.

- **History Management**: Maintains a chat history to provide continuity in conversations and improve user experience.

- **Dynamic Interface**: The application offers a dynamic user interface where users can input messages, receive responses, and visualize the conversation history in real-time.

## Installation

To run this application locally, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/chat-with-websites.git
   ```

2. **Navigate to the Project Directory**: Open a terminal window and navigate to the project directory:

   ```bash
   cd chat-with-websites
   ```

3. **Install Dependencies**: Install the required Python dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**: Start the Streamlit application by executing the following command:

   ```bash
   streamlit run app.py
   ```

## Usage

1. **Enter Website URL**: Provide the URL of the website you wish to interact with in the sidebar.
  
2. **Initiate Conversation**: Type your message in the chat input box and press Enter to initiate the conversation.

3. **View Responses**: The AI-powered chatbot will generate responses based on the context and input provided by the user.

4. **Review Conversation History**: The application maintains a history of the conversation, allowing users to review past interactions.

## Contributing

Contributions are welcomed and appreciated! To contribute to this project, follow these steps:

1. **Fork the Repository**: Fork the repository to your GitHub account.
  
2. **Create a New Branch**: Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes**: Implement your changes and ensure they adhere to the project's coding conventions.

4. **Commit Changes**: Commit your changes with descriptive commit messages:

   ```bash
   git commit -am 'Add some feature'
   ```

5. **Push to the Branch**: Push your changes to your forked repository:

   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create Pull Request**: Submit a pull request to the main repository's `main` branch.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [OpenAI](https://openai.com/)
- [langchain](https://github.com/langchain)
