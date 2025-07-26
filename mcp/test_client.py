import asyncio
from fastmcp import Client

async def main():
    # Connect to your running MCP server via stdio
    # The server script path should be relative to where you run this client
    async with Client("server.py") as client:
        # List available tools
        tools = await client.list_tools()
        print("Available tools:", tools)

        # Call the 'add' tool
        result = await client.call_tool("add", {"a": 5, "b": 3})
        print("add(5, 3) =", result.content)

        # Call the 'subtract' tool
        result = await client.call_tool("subtract", {"a": 10, "b": 4})
        print("subtract(10, 4) =", result.content)

        # Call the 'multiply' tool
        result = await client.call_tool("multiply", {"a": 6, "b": 7})
        print("multiply(6, 7) =", result.content)

        # Call the 'divide' tool
        result = await client.call_tool("divide", {"a": 20, "b": 5})
        print("divide(20, 5) =", result.content)

if __name__ == "__main__":
    asyncio.run(main()) 