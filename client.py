import requests
import streamlit as st

def get_openai_response(input_text):
    try:
        response = requests.post("http://localhost:8000/essay/invoke",
                                 json={'input': {'topic': input_text}})
        response.raise_for_status()  # Check for HTTP errors
        return response.json().get('output', {}).get('content', 'No content found')
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return None
    except ValueError as e:
        st.error(f"Error parsing JSON response: {e}")
        st.error(f"Response content: {response.content}")
        return None

def get_ollama_response(input_text):
    try:
        response = requests.post("http://localhost:8000/poem/invoke",
                                 json={'input': {'topic': input_text}})
        response.raise_for_status()  # Check for HTTP errors
        return response.json().get('output', 'No output found')
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return None
    except ValueError as e:
        st.error(f"Error parsing JSON response: {e}")
        st.error(f"Response content: {response.content}")
        return None

## Streamlit framework

st.title('Langchain Demo With LLAMA2 API')
input_text = st.text_input("Write an essay on")
input_text1 = st.text_input("Write a poem on")
if input_text:
    essay_output = get_openai_response(input_text)
    if essay_output:
        st.write(essay_output)

if input_text1:
    poem_output = get_ollama_response(input_text1)
    if poem_output:
        st.write(poem_output)
