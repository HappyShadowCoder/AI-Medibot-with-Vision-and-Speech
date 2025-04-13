import os
from dotenv import load_dotenv
from groq import Groq
import base64

# Load environment variables from .env file
load_dotenv()
#print("API KEY:", os.getenv("GROQ_API_KEY"))  # Just for debugging

# Set up the API key
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
model= "llama-3.2-90b-vision-preview"
# image_path = "acne.jpeg"
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    
def analyze_image_with_query(query , model , encoded_image):
    client = Groq(api_key=GROQ_API_KEY)
    messages = [
    {
        "role": "user",
        "content": [
           { 
               "type": "text",
               "text":query
            },
            {
                "type": "image_url",
                "image_url": {
                    "url" : f"data:image/jpeg;base64,{encoded_image}",
                }
            }
        ]
    }]
    chat_completion = client.chat.completions.create(
    messages=messages,
    model=model,
    )
    return chat_completion.choices[0].message.content

# Setup Multimodal LLM

