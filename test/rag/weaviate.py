# 这里是测试将向量数据存储到 Weaviate 中的代码  
# console:https://console.weaviate.cloud/dashboard
import weaviate
import os
  
# Set these environment variables
URL = os.getenv("WCS_URL")
APIKEY = os.getenv("WCS_API_KEY")
  
# Connect to a WCS instance
auth_config = weaviate.AuthApiKey(api_key=APIKEY)

client = weaviate.Client(
  url=URL,
  auth_client_secret=auth_config
)

