import os
import json
import streamlit as st

from pathlib import Path
from streamlit_chat import message

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.schema import SystemMessage
from langchain.prompts.chat import HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback
import langchain.prompts as prompts


def get_data():
    data_folder = Path("data")
    file_path = data_folder / "ACME_all_files.json"

    # Opening JSON file
    f = open(file_path)
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    
    # Closing file
    f.close()
    return data

def api_call():
    os.environ['OPENAI_API_KEY'] = ''

    qa_prompt = prompts.PromptTemplate(
    input_variables=["question", "context_str"],
    template="""The provided data has financial and non financial information for a company that is applying to a loan. 
    Please elaborate on this information to create a comprehensive summary of at least 200 words divided into 
    three sections: business summary, application information, financial summary. 
    The business summary should explain who the business is and the area they operate in. 
    The application information should describe the details of the requested loan including loan amount, purpose, term. 
    Comment on whether collateral offered is acceptable specifying the loan to value percentage numerically.
    Comment whether upcoming profit projections are realistic given previous profits. 
    The financial summary should highlight trends in financial accounts, statements and credit history with
    quantitative evidence. If there are any defaults add an extra paragraph with details about the default.
    \n\n
        {context_str}\n
        Question: {question}\n
        Answer: """,
    )
    return qa_prompt


def make_chain(prompt, llm):
    if type(llm) == ChatOpenAI:
        system_message_prompt = SystemMessage(
            content="""Answer like a relationship manager from a prestigius bank which has  
                       high attention to details and creates great summary reports.""",
        )
        human_message_prompt = HumanMessagePromptTemplate(prompt=prompt)
        prompt = ChatPromptTemplate.from_messages(
            [system_message_prompt, human_message_prompt]
        )
    return LLMChain(prompt=prompt, llm=llm)


def get_gpt_response(qa_prompt, data):
    llm = ChatOpenAI(temperature=0.1, model="gpt-3.5-turbo")
    qa_chain = make_chain(prompt=qa_prompt, llm=llm)
    query = 'Generate the summary'
    docs = data
    tokens = 0 
    with get_openai_callback() as cb:
        answer_text = qa_chain.run(
            question=query, context_str= docs, length=50
        )
        tokens += cb.total_tokens
    
    return answer_text

st.title("NatWest Intelligence Agent")

# Display the chatbot response
# if st.button("Submit"):

data = get_data()
qa_prompt = api_call()

answer_text = get_gpt_response(qa_prompt=qa_prompt, data=data)
st.write("Agent: ", answer_text)