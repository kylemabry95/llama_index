"""The follwoing code is used to generate images using OpenAI's DALL-E API."""
import os
from io import BytesIO
from fastapi.responses import StreamingResponse
import openai
import requests
from dotenv import load_dotenv
from PIL import Image

# Bring in our env vars
load_dotenv("keys.env")

# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate(text):
    """This function generates an image based on the provided text using OpenAI's DALL-E API."""
    generated_image = openai.images.generate(prompt=text, n=1, size="256x256")

    # Extracting the URL of the generated image
    image_url = generated_image.data[0].url

    # using requests library to get the image in bytes
    image = requests.get(image_url, timeout=15).raw

    with open("./data/generated_image.png", 'rb') as f:
        image = image.read()

    response = StreamingResponse(content=image)

    return response
