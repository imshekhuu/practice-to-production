from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-3B-Instruct",
    task="text-generation"
)

prompt = PromptTemplate(
    input_variables=["resume_text", "role"],
    template="""
You are a professional career coach.

The job role has already been predicted by a machine learning model.
Do NOT guess the role yourself.

Predicted Job Role:
{role}

Resume:
{resume_text}

Provide your response under these headings only:

Missing Skills:
- 

Improvements:
- 

Learning Roadmap:
- 
"""
)

model = ChatHuggingFace(llm=llm)

formatted_prompt = prompt.format(
    role="ML engineer",
    resume_text="docker, git, github, pandas, numpy"
)

result = model.invoke(formatted_prompt)
print(result.content)
