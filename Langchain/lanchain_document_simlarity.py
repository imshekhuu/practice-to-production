from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
    "Virat Kohli is a world-class Indian international cricketer who is widely regarded as one of the greatest batsmen of all time",
    "MS Dhoni is a world-class Indian international cricketer who is widely regarded as one of the greatest captains of all time in Indian cricket history",
    "Rohit Sharma is a world-class Indian international cricketer who is widely regarded as one of the greatest batsmen and successful captain of all time",
    "Jasprit Bumrah is a world-class Indian international cricketer who is widely regarded as one of the greatest bowlers of all time",
]

query = "tell me about Bumrah"

doc_emb = embeddings.embed_documents(documents)
query_emb = embeddings.embed_query(query)

scores = cosine_similarity([query_emb], doc_emb)[0]

index , score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

print(documents[index])
print("similarity score is: ", score)