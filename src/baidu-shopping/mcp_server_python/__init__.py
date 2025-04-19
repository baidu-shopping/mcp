# __init__.py
from .shopping import mcp

def main():
    """ Baidu Shopping MCP Server - HTTP call Baidu Shopping API for MCP"""
    mcp.run()

if __name__ == "__main__":
    main()