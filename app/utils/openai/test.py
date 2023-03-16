"""
OPENAI API 사용 테스트
"""


import openai
from app.core.config import settings

openai.organization = settings.OPENAI_ORG
openai.api_key = settings.OPENAI_API_KEY
# print(f"MODEL 갯수: {len(openai.Model.list())}")
# print(f"Model: {openai.Model.list()}")

response = openai.Image.create(
    prompt="Three children around 5 years old are playing house on the playground",
    n=1,
    size="1024x1024",
)


image_url = response["data"][0]["url"]
print(image_url)
