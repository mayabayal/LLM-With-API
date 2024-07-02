# LLM-API-Langchain-FastAPI/

# LLM API with Langchain and FastAPI

This project demonstrates how to build production-grade APIs for large language models (LLMs) using Langchain and FastAPI.

## Features
- API endpoints for OpenAI and LLaMa models
- Integration with Streamlit for frontend interface
- Utilizes LangServe for easy API creation

## Setup
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables in `.env`
4. Run the FastAPI server: `python app.py --reload`
5. Run the Streamlit app: `streamlit run client.py`

## Project Structure
- `API/main.py`: FastAPI server setup
- `API/client.py`: API routes
- Streamlit front-end application
