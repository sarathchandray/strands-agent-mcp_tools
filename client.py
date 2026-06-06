import asyncio

from mcp.client.stdio import stdio_client
from mcp import StdioServerParameters
from strands import Agent
from strands.tools.mcp.mcp_client import MCPClient
from strands.models import BedrockModel

def create_stdio_transport():
    return stdio_client(
        StdioServerParameters(
            command="python",
            args=["server.py"]
        )
    )


async def main():

    mcp_client = MCPClient(create_stdio_transport)

    try:
        # ❌ DO NOT call start()
        tools = await mcp_client.load_tools()
        print("Loaded tools:")

        for tool in tools:
            print(tool.__dict__)

        model = BedrockModel(
            model_id="amazon.nova-lite-v1:0",
            region_name="us-east-1"
        )

        agent = Agent(
            model=model,
            tools=tools
        )

        result = await agent.invoke_async("What is addition and multiplication of 10 and 20 and what is temperature in Vizag, India?")
        print(result)

    finally:
        # safe cleanup
        mcp_client.stop(None, None, None)


if __name__ == "__main__":
    asyncio.run(main())