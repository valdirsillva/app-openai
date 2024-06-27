import os
import json
import base64
import requests

from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

api_key =  os.getenv('API_KEY')

def handle_open_ai(content):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4o",
        "messages": [{ "role": "user", "content": f"{content}" } ],
        "max_tokens": 800
    }

    payload = json.dumps(payload)
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, data=payload)
    response_dict = response.json()

    output_file_path = "dados.json"

    with open(output_file_path, "w") as output_file:
        json.dump(response_dict, output_file, indent=4)
