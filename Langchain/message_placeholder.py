from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage

load_dotenv()

chat_tempate = ChatPromptTemplate([
    ('system', 'you are a helpfulcustomer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-3B-Instruct",
    task="text-generation"
)

chat_history =[]
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

chat_tempate.invoke({'chat_history': chat_history, 'query': 'whare is my refund'})
model = ChatHuggingFace(llm=llm)