
from zhipuai import ZhipuAI
from dotenv import load_dotenv
import os

API_KEY = os.getenv("ZHIPU_API_KEY")
print("API_KEY: ", API_KEY)

client = ZhipuAI(api_key=API_KEY) # 填写您自己的APIKey

customMessages=[
        {
            "role": "user",
            "content": "请你作为诗人，写一篇短篇诗歌，主题是要永远保持一颗善良的心，要能够激发儿童的学习兴趣和想象力，同时也能够帮助儿童更好地理解和接受故事中所蕴含的道理和价值观。字数限制在50个字"
        }
]

customMessages1 =[{
    "role": "user",
    "content": "我现在要去厨房，猜猜我可能要干什么"
}]


customTemperature = 0.99

response = client.chat.completions.create(
    model="glm-4",  # 填写需要调用的模型名称
    messages=customMessages1,
    # stream=True,
    temperature=customTemperature,

)
print(response)

# stream模式下，回答是分段返回的
# for chunk in response:
#     print(chunk.choices[0].delta)