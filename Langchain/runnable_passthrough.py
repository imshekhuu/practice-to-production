from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-3B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)


prompt = PromptTemplate(
    template= "write a joke {about}",
    input_variables=['about']
)

prompt2 = PromptTemplate(
    template= "explain the following joke {text}",
    input_variables=['text']
)

parser = StrOutputParser()


joke_gen = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)
})


final_chain = RunnableSequence(joke_gen, parallel_chain)

result = final_chain.invoke({'about': 'cricket'})
print(result)


