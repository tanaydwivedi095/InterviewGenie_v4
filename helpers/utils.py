from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
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

def load_previous_conversation():
    conversation = ""
    with open(r"artifacts\previous_conversation.txt", "r") as f:
        lines = f.readlines()
        conversation = "\n".join(lines)
    return conversation

def humanify(text):
    llm = load_llm()
    prompt = f"""
    You are a skilled language assistant whose sole task is to “humanify” the input text.  
    Your goal is to preserve every fact, nuance, and detail while rewriting the text so it sounds like a real person speaking.  
    
    Guidelines:
    - Do not add new information, opinions, or examples.  
    - Maintain the original intent, tone, and structure as closely as possible.  
    - Use natural phrasing, contractions, and rhythm common in everyday conversation.  
    - Ensure clarity and readability, avoiding overly formal or robotic language.  
    
    Here is the AI-generated text to humanify:
    ---
    {text}
    ---
    Please respond only with the humanified version, and nothing else.
    """
    humanified_text = llm.invoke(prompt)
    return humanified_text.content
