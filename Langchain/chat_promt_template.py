from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

chat_template = ChatPromptTemplate([
    ('system', 'you are a helpful {domain} expert'),
    ('human', 'explain in simple term, what is {topic}')
]
)

promt = chat_template.invoke({'domian' : 'cricket', 'topic': 'dusra'})
print(promt)
