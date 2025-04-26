from langchain_community.tools import TavilySearchResults
import os
from dotenv import load_dotenv
from typing import List
from src.project.state.state import State
load_dotenv()


os.environ["TAVILY_API_KEY"]=os.getenv("TAVILY_API_KEY")

class Tools:
    """ Tool for the project. """
    def __init__(self, query: str):
        self.query = query
        
    def run_tavily_search(self) -> List:  
        """ Run the Tavily search tool. """
        tavily_tool = TavilySearchResults(
            max_results=5,
            include_answer=True,
            include_raw_content=True,
            include_images=False
        )
        results = tavily_tool.run(self.query)
        return results