# shopping.py
import os
import copy
import httpx
from asyncio import sleep
 
from mcp.server.fastmcp import FastMCP, Context
 
# 创建MCP服务器实例
mcp = FastMCP("mcp-server-baidu-shopping")
'''

获取环境变量中的API密钥, 用于调用百度优选API
环境变量名为: BAIDU_SHOPPING_API_KEY, 在客户端侧通过配置文件进行设置传入
获取方式请参考: https://cloud.baidu.com/doc/UDC/index.html

'''

api_key = os.getenv('BAIDU_SHOPPING_API_KEY')
api_url = "https://mcp-youxuan.baidu.com"
 
@mcp.tool()
async def brand_rank(
    ctx: Context,
    query: str
) -> dict:
    """
    Name:
        榜单服务
    Description:
        榜单服务
    Args:
        query: 冰箱排行榜
    """
    try:
        # 获取API密钥
        if not api_key:
            raise Exception("Can not found API key.")
 
        # 调用百度API
        url = f"{api_url}/openapi/brand"
        
        # 设置请求参数
        params = {
            "key": f"{api_key}",
            "query": f"{query}",
            "from": "py_mcp"
        }
 
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            result = response.json()
 
        if result.get("errno") != 0:
            error_msg = result.get("errmsg", "unkown error")
            raise Exception(f"API response error: {error_msg}")
        
        data = result.get("data", {})
        return data

    except httpx.HTTPError as e:
        raise Exception(f"HTTP request failed: {str(e)}") from e
    except KeyError as e:
        raise Exception(f"Failed to parse reponse: {str(e)}") from e
 
@mcp.tool()
async def param_compare(
    ctx: Context,
    query: str
) -> dict:
    """
    Name:
        参数对比服务
    Description:
        参数对比服务
    Args:
        query: iphone16和iphone15对比
    """
    try:
        # 获取API密钥
        if not api_key:
            raise Exception("Can not found API key.")
 
        # 调用百度API
        url = f"{api_url}/openapi/param"
        
        # 设置请求参数
        params = {
            "key": f"{api_key}",
            "query": f"{query}",
            "from": "py_mcp"
        }
 
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            result = response.json()
 
        if result.get("errno") != 0:
            error_msg = result.get("errmsg", "unkown error")
            raise Exception(f"API response error: {error_msg}")
        
        data = result.get("data", {})
        return data

    except httpx.HTTPError as e:
        raise Exception(f"HTTP request failed: {str(e)}") from e
    except KeyError as e:
        raise Exception(f"Failed to parse reponse: {str(e)}") from e
 
if __name__ == "__main__":
    mcp.run()