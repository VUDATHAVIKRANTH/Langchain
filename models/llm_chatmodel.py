from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()



model= ChatGoogleGenerativeAI(model='gemini-1.5-pro')

result = model.invoke('explain how gemini studio works in few words')

print(result.content)