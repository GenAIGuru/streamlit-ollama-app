import ollama
import streamlit as st
import torch

# Constants
MESSAGES_KEY = "messages"
MODEL_KEY = "model"


def initialize_session_state():
    """Initialize the session state if it doesn't exist."""
    if MESSAGES_KEY not in st.session_state:
        st.session_state[MESSAGES_KEY] = []

    if MODEL_KEY not in st.session_state:
        st.session_state[MODEL_KEY] = ""


def get_available_models():
    """Retrieve the list of available models from the ollama library."""
    return [model["name"] for model in ollama.list()["models"]]


def select_model():
    """Allow the user to select a model from the available options."""
    models = get_available_models()
    st.session_state[MODEL_KEY] = st.selectbox("Choose your model", models)


@st.cache_resource
def get_device():
    """Determine the appropriate device (GPU or CPU) for model inference."""
    if torch.cuda.is_available():
        return torch.device("cuda")
    else:
        return torch.device("cpu")


def model_res_generator():
    """Generate the model response using the selected model and message history."""
    device = get_device()
    stream = ollama.chat(
        model=st.session_state[MODEL_KEY],
        messages=st.session_state[MESSAGES_KEY],
        stream=True,
    )
    for chunk in stream:
        yield chunk["message"]["content"]


def display_chat_history():
    """Display the chat messages from the history on app rerun."""
    for message in st.session_state[MESSAGES_KEY]:
        with st.chat_message(message["role"]):
            st.write(message["content"])


def handle_user_input():
    """Handle the user's input and update the message history."""
    if prompt := st.chat_input("Enter prompt here.."):
        st.session_state[MESSAGES_KEY].append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            ai_response = st.write_stream(model_res_generator())
            st.session_state[MESSAGES_KEY].append({"role": "assistant", "content": ai_response})



def main():
    st.title("My Personal Chatbot")
    initialize_session_state()
    select_model()
    display_chat_history()
    handle_user_input()


if __name__ == "__main__":
    main()
