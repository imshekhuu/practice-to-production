from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text = "dfhbgiuhgper ehgeriuhearoihgpdj erhgerogargsjgodfbj reiguhrogihdighotobn bidufjgiudfhjhb bhfhgoijgouidg fdihodufhgoisgjpsogjoxb iuhbdiughsoi t ohoisehtoisehgshg"
vector = embeddings.embed_query(text)

print(len(vector))
print(vector[:10])  # first 10 values
