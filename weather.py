from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool()
def getweather(location: str) -> str:
        """Get the current weather information for the specified city or location."""
        return f"The weather is always sunny in {location}"

if __name__ == "__main__":
        mcp.run(transport="streamable-http")