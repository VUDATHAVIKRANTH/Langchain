from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model ='text-embedding-3-large', dimension=32)

documents=[]

query=""


document_emb = embedding.embed_documents(documents)

query_emb = embedding.embed_query(query)

scores = cosine_similarity([query_emb],document_emb)

index, score =sorted(list(enumerate(scores)),key=lambda x: x[1])[-1]

print(documents[index])
print("similarity score=",score)