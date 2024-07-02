from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes  # Ensure this import is correct
import uvicorn
import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama

# Load environment variables from .env file
load_dotenv()

# Set environment variables
open_api_key = os.getenv("OPENAI_API_KEY")
if not open_api_key:
    raise ValueError("OPEN_API_KEY environment variable is not set")
os.environ['OPEN_API_KEY'] = open_api_key

# Initialize FastAPI app
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)

# Add routes
add_routes(app, ChatOpenAI(), path="/openai")

model = ChatOpenAI()
llm = Ollama(model="llama2")

prompt1 = ChatPromptTemplate.from_template("write me an essay about {topic} with 200 words")
prompt2 = ChatPromptTemplate.from_template("write me a poem about {topic} with 200 words")

add_routes(app, prompt1 | model, path="/essay")
add_routes(app, prompt2 | llm, path="/poem")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
