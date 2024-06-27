
import json
from fastapi import FastAPI
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware
from src.openai.index import handle_open_ai

app = FastAPI(title="Project Openai", openapi_tags=[
                  {  "name": "visualizar", "description": "" },
                  {  "name": "Código", "description": "" }
              ])

origins = [
    "http://127.0.0.1:5500",
    "http://localhost:8000",
    "https://localhost:8000",
    "https://localhost:3003",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputContent(BaseModel):
    content: str

@app.post("/openai/")
def post_openai(input_content: InputContent):
    input = input_content.content

    if len(input) > 0:
        handle_open_ai(input)

@app.get("/openai/")
def get_openai():
    output_file_path = "dados.json"

    with open(output_file_path, "r") as input_file:
        data = json.load(input_file)

    return data
    
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", reload=True)

