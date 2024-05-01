# Streamlit Ollama Chatbot

This is a Streamlit application that creates a personal chatbot using the Ollama library.
You can run this application locally and enjoy Generative AI without the need of external library.
The chatbot allows users to interact with a large language model and view the conversation history.
Code has been improved using Amazon Q Developer.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#Usage)
3. [Contributing](#Contributing)
4. [Submitting Changes](#Submitting)
5. [Issue and Feedback](#Feedback)
6. [License](#license)

## Installation

To set up the Streamlit Ollama Chatbot application, follow these steps:

1. **Clone Repository**: Use Git to clone the repository:
   ```
   git clone https://github.com/GenAIGuru/streamlit-ollama-app.git
   ```

2. **Create virtual env**: Set up a virtual environment using Conda or venv:
    ```
    conda create -n ollama python=3.7  
    ```
3. **Activate Environment:**
   ```
   conda activate ollama
   ```
4. **Download models**:  Obtain models from Ollama's library. Visit https://ollama.com/library to download the desired models and use the following command to pull a specific model:
    ```
    ollama pull model_name_here
    ```
5. **Install Dependencies**: Install the required Python packages by running the following command in your terminal:

    ```
    pip install -r requirements.txt
    ```
   
## Usage

To run the Streamlit Ollama Chatbot, execute the following command in your terminal:
    ```
    streamlit run ollama_app.py
    ```

## Contributing

We welcome contributions to the Streamlit Ollama Chatbot project! If you'd like to contribute, please follow these guidelines:

1- **Fork the repository and create a new branch** for your changes.

2- **Install the project dependencies** by running 
    ```
    pip install -r requirements.txt
    ```

3- **Make your changes** and ensure the application still runs correctly by executing 
    ```
    streamlit run ollama_app.py
    ```

## Submitting

Test your changes thoroughly and ensure they don't break any existing functionality.

Update the documentation, including the README.md file, to reflect any changes you've made.

Commit your changes and push your branch to your forked repository.

Open a pull request to the main repository, describing the changes you've made and why they're valuable.

## Feedback

If you encounter any issues or have suggestions for improvements, please open an issue in the repository. We'll do our best to address them in a timely manner.

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute the code as long as you include the original copyright and license notice.

