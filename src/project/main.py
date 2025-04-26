import streamlit as st
from src.project.ui.streamlitui import StreamlitUI


def main():
    """Main function to run the Streamlit UI and workflow"""
    # Initialize the UI
    ui = StreamlitUI()
    ui.initialize_session_state()
    st.title("AI agent-based Deep Research")
    
    if st.session_state.current_node == "initialization":
        ui.display_ui()
        if st.session_state.get("query"):
            st.session_state.current_node = "handel_graphflow"
            st.rerun()
    elif st.session_state.current_node == "handel_graphflow":
        ui.handle_graphflow()
   


