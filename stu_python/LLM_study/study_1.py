from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o",
    message=[
        {"role": "system", "content": "あなたは優秀なアシスタントです。"},
        {"role": "system", "content":"情報苦学の観点から,APIについて1文で教えて。"}
    ]
)

answer = response.choices[0].message.content
print(answer)