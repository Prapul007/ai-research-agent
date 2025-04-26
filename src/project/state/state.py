from pydantic import BaseModel
from typing import Optional, Dict, Any, List

class State(BaseModel):
    """ State class for the project. """
    query : str
    tool_results : str
    research_results : str
    final_answer : str
    