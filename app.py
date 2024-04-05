import os
from dotenv import load_dotenv
from langchain_community.llms.openai import OpenAI
from langchain.text_splitter import TextSplitter
from langchain.chains import llm
from langchain.prompts import PromptTemplate

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


def generate_brd(text):
    temperature = 0.5
    llm=OpenAI(temperature=temperature)
    prompt = PromptTemplate(input_variables=['text'], template='You are a software engineer at a tech company. You are tasked with writing a business requirements document (BRD) for the following requirements: \n\n{text}')

    res=prompt.format(text=text)
    result=llm(res,max_tokens=2000)
    return result













