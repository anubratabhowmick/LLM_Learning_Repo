import argparse
import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_image(image_url1, image_url2, question):
    """
    Analyze an image and answer a question about it
    
    Args:
        image_url1 (str): The URL of the first image to analyze
        image_url2 (str): The URL of the second image to analyze
        question (str): The question to answer about the image
    Returns:
        answer (str): The answer to the question
    """
    messages=[
            {"role": "user", "content": [
                {"type": "text", "text": question},
                {"type": "image_url", "image_url": {"url": image_url1}},
                {"type": "image_url", "image_url": {"url": image_url2}}
            ]}
        ]
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Image QA")
    parser.add_argument("--image_url1", type=str, help="First Image URL")
    parser.add_argument("--image_url2", type=str, help="Second Image URL")
    parser.add_argument("--question", type=str, help="Question about the image")
    args = parser.parse_args()
    
    answer = analyze_image(args.image_url1, args.image_url2, args.question)
    print(answer)
    
    
    