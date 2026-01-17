from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnableParallel, RunnablePassthrough, RunnableBranch

load_dotenv()

def count(text):
    return len(text.split())

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-3B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)


prompt = PromptTemplate(
    template= "write a detaild report on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template= "summerize the following text {text}",
    input_variables=['text']
)

parser = StrOutputParser()

gen_topic = RunnableSequence(prompt, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 300, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)


final_chain = RunnableSequence(gen_topic, branch_chain)

result = final_chain.invoke({'topic': 'Russia vs Ukraine'})
print(result)