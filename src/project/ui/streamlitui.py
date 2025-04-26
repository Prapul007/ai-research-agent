import streamlit as st
from src.project.state.state import State
from src.project.graph.graph_builder import GraphBuilder
from src.project.utils.markdown import clean_markdown


@st.cache_resource
def get_graph():
    builder = GraphBuilder()
    return builder.agentic_system()
    
class StreamlitUI:
    """ Streamlit UI for the project."""
    def __init__(self):
        self.initialize_session_state()
        self.graph = get_graph()  
        
    def initialize_session_state(self):
        if "query" not in st.session_state:
            st.session_state.query = ""
        if "current_node" not in st.session_state:
            st.session_state.current_node = "initialization"

    def display_ui(self):
        """ Display the Streamlit UI. """
        query = st.text_area(
            "Enter your query:",
            value=st.session_state.query,
            height=150,
            help="Describe your query."
        )

        if st.button("Submit", use_container_width=True):
            if not query:
                st.error("Please enter a project name.")
                return
            try:
                st.session_state.query = query
                st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")
        
    def handle_graphflow(self):
        """ Handle the graph flow. """
        with st.spinner("Performing research..."):
            try:
                initial_state = State(
                    query=st.session_state.query,
                    tool_results="",
                    research_results="",
                    final_answer=""
                )
                result = self.graph.invoke(
                    initial_state.model_dump()
                )
            except Exception as e:
                st.error(f"An error occurred: {e}")
                return
            
        st.markdown(clean_markdown(result), unsafe_allow_html=True)

                
            