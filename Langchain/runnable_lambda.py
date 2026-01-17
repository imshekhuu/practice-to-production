from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnableParallel, RunnablePassthrough

load_dotenv()

def count(text):
    return len(text.split())

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-3B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)


prompt = PromptTemplate(
    template= "write a joke {about}",
    input_variables=['about']
)

parser = StrOutputParser()

joke_gen = RunnableSequence(prompt, model, parser)

chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'count': RunnableLambda(count)
})


final_chain = RunnableSequence(joke_gen, chain)
result = final_chain.invoke({'about':'cricket'})
print(result)