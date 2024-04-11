from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.llms.openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores.chroma import Chroma
from langchain.chains.summarize import load_summarize_chain
from langchain_community.embeddings.sentence_transformer import (SentenceTransformerEmbeddings)
from langchain_community.document_loaders.pdf import PyPDFLoader
from dotenv import load_dotenv
import os
from tempfile import NamedTemporaryFile

load_dotenv()   
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
llm = OpenAI(temperature=0.9)

def get_chunks(text):
    splitter = RecursiveCharacterTextSplitter()
    chunks = splitter.split(text)
    return chunks

def generate_test_cases(brd_file_upload):
    temp_file = NamedTemporaryFile(delete=False)
    temp_file.write(brd_file_upload.read())
    temp_file.close()

    brd_file = temp_file.name
    loader = PyPDFLoader(brd_file)
    documents = loader.load()   
    docs= get_chunks(documents)

    embedding= SentenceTransformerEmbeddings(model_name='all-MiniLM-L6-v2')
    db = Chroma.from_documents(docs, embedding)

    query = 'find introduction, requirements, functional requirements, non-functional requirements'
    docs = db.similarity_search(query)
    chain = load_summarize_chain(llm, chain_type='stuff')
    summary = chain.run(docs)

    prompt = PromptTemplate(input_variables=['text'], template='You are a software engineer, business analyst, ai developer, data analyst at a tech company and an expert at writing test cases. You are tasked with writing test cases for the following requirements or summary: \n\n{text}')
    res = prompt.format(text=summary)
    result = llm(res,max_tokens=3500)
    return result