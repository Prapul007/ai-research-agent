def clean_markdown(result):
    """
    Cleans research results into properly formatted markdown structure.
    """

    def extract_content(obj):
        # Safely get content
        if hasattr(obj, "content"):
            return obj.content
        else:
            return str(obj)  # fallback

    # Extract data
    query = result.get("query", "No query provided")
    research_results = extract_content(result.get("research_results", "No research results available"))
    final_answer = extract_content(result.get("final_answer", "No final answer available"))

    # Clean whitespace
    query = query.strip()
    research_results = research_results.strip()
    final_answer = final_answer.strip()

    # Format Markdown cleanly
    markdown_content = f"""# Research Results

## Original Query
{query}

## Research Findings
{research_results}

## Final Answer
{final_answer}
"""
    return markdown_content
