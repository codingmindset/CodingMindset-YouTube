import os
import gradio as gr
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from dotenv import load_dotenv
import logging

# Load environment variables from a .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_api_key():
    """
    Retrieves the Mistral API key from environment variables.
    
    Returns:
    str: The API key.
    """
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        logging.error("MISTRAL_API_KEY environment variable not found.")
        raise ValueError("API key not found. Please set the MISTRAL_API_KEY environment variable.")
    return api_key

def create_mistral_client(api_key):
    """
    Creates a MistralClient instance.
    
    Args:
    api_key (str): The API key for authentication.
    
    Returns:
    MistralClient: The MistralClient instance.
    """
    try:
        return MistralClient(api_key=api_key)
    except Exception as e:
        logging.error(f"Error creating MistralClient: {e}")
        raise

def get_chat_response(client, user_input, model="codestral-mamba-latest"):
    """
    Gets the chat response from the Mistral API.
    
    Args:
    client (MistralClient): The MistralClient instance.
    user_input (str): The input message from the user.
    model (str): The model name.
    
    Returns:
    str: The response message from the Mistral API.
    """
    try:
        messages = [ChatMessage(role="user", content=user_input)]
        chat_response = client.chat(model=model, messages=messages)
        return chat_response.choices[0].message.content
    except Exception as e:
        logging.error(f"Error interacting with the Mistral API: {e}")
        return "An error occurred while interacting with the Mistral API. Please try again later."

def chat_with_mistral(user_input):
    """
    Function to interact with the Mistral API.
    
    Args:
    user_input (str): The input message from the user.
    
    Returns:
    str: The response message from the Mistral API.
    """
    try:
        api_key = get_api_key()
        client = create_mistral_client(api_key)
        return get_chat_response(client, user_input)
    except ValueError as e:
        return str(e)
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return "An unexpected error occurred. Please try again later."

def create_gradio_interface():
    """
    Creates and launches the Gradio interface.
    """
    ui = gr.Interface(
        fn=chat_with_mistral,
        inputs=gr.components.Textbox(label="Enter Your Message"),
        outputs=gr.components.Markdown(label="Chatbot Response"),
        title="Mistral Coding Assistant",
        description="Get coding help and advice from the Mistral API. Enter your programming questions or code snippets and receive assistance.",
        examples=[
            ["How do I reverse a string in Python?"],
            ["Can you explain the difference between a list and a tuple in Python?"]
        ],
        allow_flagging="never"
    )
    ui.launch()

if __name__ == "__main__":
    create_gradio_interface()