from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo", temperature=0.7, max_tokens=1500)

result=llm.invoke("what is the Capital of Andhra Pradesh?")

print(result)
