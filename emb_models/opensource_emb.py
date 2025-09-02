from langchain_huggingface import HuggingFaceEmbeddings

embedding= HuggingFaceEmbeddings(model_name='')

result = embedding.embed_query("Give top5 companies that work in Agentic AI field")

print(result)