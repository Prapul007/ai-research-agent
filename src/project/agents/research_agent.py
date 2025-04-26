from src.project.state.state import State
from src.project.tools.tavily_tool import Tools


class ResearchAgent:
    def __init__(self, model):
        """
        Initializes the Research Agent with the given LLM model.
        """
        self.llm = model

    def research_agent(self, state: State):
        """
        Researches a query and processes the results.
        
        Args:
            state (State): The current state containing the query
            
        Returns:
            Updated state with research_results populated
        """
        query = state.query
        tool = Tools(query=query)
        
        # Use the Tavily tool to perform the research
        results = tool.run_tavily_search()
        
        # Store raw results in the state
        state.tool_results = str(results)
        
        # Process the results and generate analysis
        prompt = """
        You are an advanced Research Agent designed to gather comprehensive information on a given query.

        Your input is a query and search results from the Tavily API containing web content.

        For each search result provided, your task is to:
        1. Extract the most relevant information related to the query
        2. Identify key facts, data points, and insights
        3. Note any contradictions or uncertainties in the source
        4. Evaluate the credibility and recency of the information
        5. Create a concise, well-structured summary that captures the essential information

        Format your response as a structured analysis with:
        - Source URL
        - Source credibility assessment (High/Medium/Low)
        - Key information extracted
        - Relevance to original query (High/Medium/Low)
        - Concise summary (2-3 paragraphs)

        After analyzing all sources, provide a brief overview of:
        - Most reliable findings
        - Knowledge gaps that need further research
        - Any conflicting information discovered

        Remember to maintain objectivity and focus on facts rather than opinions.
        Give your response in markdown format, including headings and bullet points where appropriate.
        """
        
        # Prepare the context with all search results for analysis
        context = f"QUERY: {query}\n\nSEARCH RESULTS:\n"
        for i, result in enumerate(results):
            context += f"\n--- RESULT {i+1} ---\n"
            context += f"URL: {result.get('url', '')}\n"
            context += f"TITLE: {result.get('title', '')}\n"
            context += f"CONTENT: {result.get('content', '')}\n"
        
        # Get comprehensive analysis from LLM
        research_analysis = self.llm.invoke(prompt + context)
        
        # Update the state with processed research results
        state.research_results = research_analysis
        
        return state