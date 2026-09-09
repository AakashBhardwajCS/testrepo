from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai_llm = OpenAI(model_name="text-davinci-003", api_key=OPENAI_API_KEY)

def ask_question(question):
    answer = openai_llm.invoke(question)
    return answer

