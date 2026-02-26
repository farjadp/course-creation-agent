from google.adk.agents import Agent
from google.adk.tools.google_search_tool import google_search


MODEL = "gemini-2.5-pro"

root_agent = Agent(
    name="researcher",
    model=MODEL,
    tools=[google_search],
    instruction=(
        "You are a research assistant. Use the google_search tool to gather "
        "accurate and up-to-date information in response to user queries. "
        "Summarize your findings clearly and cite your sources."
    ),
)

