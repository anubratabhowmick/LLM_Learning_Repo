import argparse
import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_prompt(text):
    """ 
    Create input prompt for the language model
    
    Args:
        text (str): The text to classify
    Returns:
        prompt (str): The input prompt for the language model
    """
    
    instructions = 'Is the underlying setiment positive or negative?'
    formatting = '"Positive" or "Negative"'
    
    return f'Text: {text}\n{instructions}\nAnswer({formatting}):'
    
def call_llm(prompt):
    """ 
    Call the language model with the input prompt to get the output
    
    Args:
        prompt (str): The input prompt for the language model
    Returns:
        response (str): The output from the language model
    """
    messages = [
        {"content": prompt, "role": "user"}
    ]
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )
    
    return response.choices[0].message.content

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sentiment Classification")
    parser.add_argument("--text", type=str, help="Text to classify")
    args = parser.parse_args()
    
    prompt = create_prompt(args.text)
    print(prompt, '\n\n')
    
    answer = call_llm(prompt)
    print(answer)
