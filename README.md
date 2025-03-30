# Learning Generative AI

## Project Overview

This repository is dedicated to exploring and learning about generative AI models and their applications. It includes various components and projects that demonstrate different functionalities and use cases of generative AI.

## Installation

To set up the project, clone the repository and install the required packages:

```bash
git clone <repository-url>
cd LLM_LEARNING_REPO
```

Each component has its own requirements. Refer to the specific component directories for their respective installation instructions.

## Environment Variables

Create a `.env` file in the root directory and add the necessary environment variables:

```ini
# For OpenAI-based components
OPENAI_API_KEY=your_openai_api_key_here

# For Pinecone-based components (required for Regulation_Chatbot)
PINECONE_API_KEY=your_pinecone_api_key_here
PINECONE_API_ENV=your_pinecone_api_env_here
```

## Components

### [Llama3.1B](Llama3.1B/README.md)
A chat application using the Llama3.1B model. Requires Ollama to be installed locally.

**Dependencies:**
- streamlit
- ollama

### [MCQ Generator](MCQ_Generator/README.md)
A tool for generating multiple-choice questions using generative AI.

**Dependencies:**
- openai
- langchain
- langchain_community
- langchain-openai
- streamlit
- python-dotenv
- PyPDF2

### [Regulation Chatbot](Regulation_Chatbot/README.md)
An end-to-end medical chatbot using the Llama2 model.

**Dependencies:**
- ctransformers==0.2.5
- sentence-transformers==2.2.2
- pinecone-client
- langchain==0.2.7
- flask
- python-dotenv
- pypdf
- langchain_community==0.2.7

### [Data Analysis with LLMs](Data%20Analysis%20with%20LLMs/README.md)
A collection of scripts for various data analysis tasks using Large Language Models.

**Dependencies:**
- argparse
- openai
- python-dotenv

### [Notebooks](Notebooks/)
A collection of Jupyter notebooks demonstrating various aspects of generative AI:

1. [test_openai_api.ipynb](Notebooks/1.%20test_openai_api.ipynb) - Testing the OpenAI API
2. [prompting_and_functions.ipynb](Notebooks/2.%20prompting_and_functions.ipynb) - Prompting techniques and functions
3. [langchain.ipynb](Notebooks/3.%20langchain.ipynb) - Introduction to LangChain
4. [huggingface_with_langchain.ipynb](Notebooks/4.%20huggingface_with_langchain.ipynb) - Using Hugging Face models with LangChain
5. [vector_database.ipynb](Notebooks/5.%20vector_database.ipynb) - Working with vector databases
6. [meta_llama.ipynb](Notebooks/6.%20meta_llama.ipynb) - Exploring Meta's Llama models
7. [financial_agent.ipynb](Notebooks/7.%20financial_agent.ipynb) - Building a financial analysis agent
8. [gemini_google.ipynb](Notebooks/8.%20gemini_google.ipynb) - Working with Google's Gemini models
9. [mistral_testing.ipynb](Notebooks/9.%20mistral_testing.ipynb) - Testing Mistral AI models
10. [litellm.ipynb](Notebooks/10.%20litellm.ipynb) - Using LiteLLM for model management
11. [warren_buffet_ai_agent.ipynb](Notebooks/11.%20warren_buffet_ai_agent.ipynb) - An AI agent mimicking Warren Buffett's investment style

## Usage

Refer to the individual component READMEs for specific usage instructions.

## Contributing

Feel free to open issues or submit pull requests to contribute to the project.

## License

This project is licensed under the MIT License.