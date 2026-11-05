import os
from dotenv import load_dotenv
load_dotenv()

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("math")

@mcp.tool()
def math(a: int, b: int) ->  str:
    """Use this function to add two values and return in this format"""
    return f"SPECIAL FORMAT: {a+b}"


@mcp.tool()
def multiplications(a: int, b: int) -> str:
    """Use this function to add two values and return in this format"""
    return f"SPECIAL FORMAT: {a*b}"


if __name__ == "__main__":
    mcp.run(transport="stdio")


