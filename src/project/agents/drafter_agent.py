from src.project.state.state import State


class DrafterAgent:
    def __init__(self, model):
        """
        Initializes the Drafter Agent with the given LLM model.
        """
        self.llm = model

    def draft_answer(self, state: State):
        """
        Synthesizes research results into a comprehensive final answer.
        
        Args:
            state (State): The current state containing research_results
            
        Returns:
            Updated state with final_answer populated
        """
        query = state.query
        research_results = state.research_results
        
        print(f"Drafting answer for: {query}")
        
        prompt = """
        You are an expert Answer Drafter responsible for creating comprehensive, accurate responses
        based on research findings. Your task is to synthesize the provided research results into
        a well-structured, authoritative answer.

        When drafting your response:
        1. Directly address all aspects of the original query
        2. Organize information logically with clear section headings when appropriate
        3. Prioritize information from more credible sources
        4. Present a balanced view that includes any conflicting perspectives found in the research
        5. Support main points with specific facts, data, and examples from the research
        6. Acknowledge limitations or gaps in the available information
        7. Use clear, precise language appropriate to the subject matter
        8. Conclude with key takeaways or a direct answer to the original query
        
        Original Query: {query}
        
        Research Findings:
        {research_results}
        
        Please draft a comprehensive, well-structured answer based on these research findings.
        Give your response in markdown format, including headings and bullet points where appropriate.
        """
        
        # Format the prompt with actual values
        formatted_prompt = prompt.format(
            query=query,
            research_results=research_results
        )
        
        # Generate the final answer
        final_answer = self.llm.invoke(formatted_prompt)
        
        # Update the state with the final answer
        state.final_answer = final_answer
        
        return state