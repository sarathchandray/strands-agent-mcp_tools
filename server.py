from mcp.server.fastmcp import FastMCP

mcp = FastMCP("demo")

@mcp.tool(
    name="calculator_add",
    description="Adds two numbers together."
)
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool(
    name="calculator_multiply",
    description="Multiplies two numbers together."
)
def multiply(a: int, b: int) -> int:
    return a * b


if __name__ == "__main__":
    mcp.run()