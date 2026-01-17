from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-3B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template= "generate a tweet about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template= "generate a linkedin post about {topic}",
    input_variables=['topic']
)

pareser = StrOutputParser()


parrell_runnable = RunnableParallel({
    'tweet' : RunnableSequence(prompt, model, pareser),
    'linkedin': RunnableSequence(prompt2, model, pareser)
})

result = parrell_runnable.invoke({'topic':'AI'})
print(result['tweet'])
print(result['linkedin'])