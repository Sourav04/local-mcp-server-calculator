from fastmcp import FastMCP

mcp = FastMCP("Calculator MCP Server")

@mcp.tool
def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b

@mcp.tool
def subtract(a: float, b: float) -> float:
    """Return the difference of a and b."""
    return a - b

@mcp.tool
def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b

@mcp.tool
def divide(a: float, b: float) -> float:
    """Return the quotient of a and b."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

if __name__ == "__main__":
    mcp.run(transport="stdio")