from langgraph.graph import StateGraph, END, START
from src.project.state.state import State
from src.project.agents.research_agent import ResearchAgent
from src.project.LLM.model import GoogleLLM
from src.project.agents.drafter_agent import DrafterAgent

class GraphBuilder:
    def __init__(self):
        self.graph_builder=StateGraph(State)        
        self.load_llm = GoogleLLM()

    
    def agentic_system(self):
        self.research_node=ResearchAgent(self.load_llm.get_google())
        self.graph_builder.add_node("Research Agent",self.research_node.research_agent)
        self.drafter_node=DrafterAgent(self.load_llm.get_google())
        self.graph_builder.add_node("Drafter Agent",self.drafter_node.draft_answer)
        
        self.graph_builder.add_edge(START,"Research Agent")
        self.graph_builder.add_edge("Research Agent", "Drafter Agent")
        self.graph_builder.add_edge("Drafter Agent", END)
        
        return self.graph_builder.compile()
    
        
        