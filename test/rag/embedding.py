from zhipuai import ZhipuAI
from dotenv import load_dotenv
import os

API_KEY = os.getenv("ZHIPU_API_KEY")

client = ZhipuAI(api_key=API_KEY) # 填写您自己的APIKey
response = client.embeddings.create(
    model="embedding-2",  # 填写需要调用的模型名称
    input="贝壳",
)
print(response)

# 将 获取到的向量进行保存到向量数据库中