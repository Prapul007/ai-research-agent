import os
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()


os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")
    
class GoogleLLM:
    """ LLM for the project. """
    def get_google(self):
        try:
            llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
        except Exception as e:
            raise ValueError(f"Error Occurred with Exception : {e}")
        return llm