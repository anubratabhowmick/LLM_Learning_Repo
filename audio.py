import argparse
import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def transcribe_audio(audio_path):
    """
    This function transcribes an audio file and returns the text.
    
    Args:
        audio_path (str): The path to the audio file
    Returns:
        text (str): The transcribed text
    """
    with open(audio_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
        
    return transcript.text

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Audio")
    parser.add_argument("--audio_file", type=str, help="Audio file")
    args = parser.parse_args()

    text = transcribe_audio(args.audio_file)
    print(text)
    