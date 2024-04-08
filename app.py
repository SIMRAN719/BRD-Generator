import os
from dotenv import load_dotenv
from langchain_community.llms.openai import OpenAI
from langchain.prompts import PromptTemplate
import time

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

class BRD_Generator:
    def __init__(self,text):
        self.llm = OpenAI(temperature=0.5)
        self.text=text

    def generate_brd(self):
        brd_result=''
        brd_topics=['Introduction','Purpose','Scope','Objectives','Stakeholders','Business Background','Overview Of Company','Functional Requirements','Non-Functional Requirements','Assumptions','Constraints','Risks','Dependencies','Project Timeline','Risk Management','References','Conclusion','Glossary of terms','Appendix','Sign-Off']
        for subtopic in brd_topics:
            prompt = PromptTemplate(input_variables=['text','subtopic'], template='You are a software engineer, business analyst, data analyst at a tech companyv and an expert at writing BRD. You are tasked with writing a business requirements document (BRD) for the following requirements: \n\n{text} on topic {subtopic}')
            res=prompt.format(text=self.text,subtopic=subtopic)
            result=self.llm(res,max_tokens=1500)
            brd_result+=subtopic+'\n'+result+'\n\n'
            time.sleep(20)
        return brd_result
    
    def table_of_contents(self):
        p1=PromptTemplate(input_variables=['text'], template='You are a software engineer, business analyst, data analyst at a tech company and an expert at writing BRD. You are tasked with writing Table of Contents on the following requirements: \n\n{text}')

        res=p1.format(text=self.text)
        result=self.llm(res,max_tokens=3000)
        return result
    
    def table_of_contents_in_lints(self):
        table_of_contents=self.table_of_contents().split('\n')
        filtered_list=[]
        for topic in table_of_contents:
            if not topic.strip():
                continue
            if topic.lower().startswith('table of contents'):
                continue

            filtered_list.append(topic.strip())
        return filtered_list













