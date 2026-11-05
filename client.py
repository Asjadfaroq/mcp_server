import os
from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio


async def main():
    client = MultiServerMCPClient(
    {
        "math": {
            "command": "python",
            "args": ["math.py"],
            "transport": "stdio"
        },
        "weather": {
            "url": "http://127.0.0.1:8000/mcp",
            "transport": "streamable_http"
        }
    })

    tools = await client.get_tools()
    agent = create_agent(
        model="groq:openai/gpt-oss-20b",
        tools=(tools)
    )

    response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
    print(response["messages"][-1].content)


    response = await agent.ainvoke({"messages": "what is the weather in Germany?"})
    print(response["messages"][-1].content)

    
if __name__ == "__main__":
    asyncio.run(main())
