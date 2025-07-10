from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
# from langchain.tools.tavily_search import TavilySearchResults
from langchain_tavily import TavilySearch
from langchain.agents import initialize_agent, Tool

load_dotenv(dotenv_path=r".env")

def load_llm():
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2
    )
    # search = TavilySearchResults()
    search = TavilySearch()
    tools = [
        Tool(
            name="Tavily Search",
            func=search.run,
            description="Search the internet using Tavily to get up-to-date info."
        )
    ]
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent="zero-shot-react-description",
        verbose=True
    )
    return agent

def load_previous_question():
    conversation = ""
    with open(r"artifacts\previous_conversation.txt", "r") as f:
        lines = f.readlines()
        conversation = "\n".join(lines)
    return conversation
