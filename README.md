# AI Research Agent with Dual-Agent Architecture

## Project Overview
This project implements an advanced AI research system using a dual-agent architecture powered by LangGraph and LangChain. The system consists of two specialized agents:
- Research Agent: Focuses on data collection and analysis using Tavily API
- Drafter Agent: Processes research findings and generates comprehensive responses

## 🛠️ Technical Architecture

### Core Components
- **Research Agent**: Handles web crawling and information gathering
- **Drafter Agent**: Processes and synthesizes research findings
- **State Management**: Uses Pydantic for robust state handling
- **Graph System**: Implements LangGraph for agent coordination

### Technologies Used
- LangChain
- LangGraph
- Streamlit
- Tavily API
- Google Gemini
- Python 3.9+

## 📋 Prerequisites
```text
- Python 3.9 or higher
- API keys for:
  - Tavily
  - Google Gemini
```

## 🔧 Installation

1. **Clone the repository**
```bash
git clone https://github.com/Prapul007/ai-research-agent.git
```

2. **Create and activate virtual environment**
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```text
Create a .env file as shown in .env.example 
```

## 🚀 Running the Application

1. **Start the Streamlit server**
```bash
streamlit run app.py
```

2. **Access the web interface**
```text
Open your browser and navigate to: http://localhost:8501
```

## 📁 Project Structure
```
ai-research-agent/
├── src/
│   ├── project/
│   │   ├── agents/
│   │   │   ├── research_agent.py
│   │   │   └── drafter_agent.py
│   │   ├── graph/
│   │   │   └── graph_builder.py
│   │   ├── LLM/
│   │   │   └── model.py
│   │   ├── state/
│   │   │   └── state.py
│   │   ├── tools/
│   │   │   └── tavily_tool.py
│   │   ├── ui/
│   │   │   └── streamlitui.py
│   │   ├── utils/
│   │   │   └── markdown.py
│   │   └── main.py
├── app.py
├── .env
├── requirements.txt
└── README.md
```

## 🔄 Workflow

1. User inputs a research query
2. Research Agent:
   - Crawls web using Tavily API
   - Collects relevant information
   - Analyzes data credibility
3. Drafter Agent:
   - Processes research findings
   - Generates structured response
   - Formats output in markdown

## 🛡️ Error Handling
- API failure recovery
- Input validation using Pydantic
- Graceful error messages
- State persistence

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch
3. Commit changes
4. Push to branch
5. Open a Pull Request

## 🙏 Acknowledgments
- LangChain team for the framework
- Tavily API for search capabilities
- Google for Gemini API

