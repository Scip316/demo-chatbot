import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
user_input = input("You: ")

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"),
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "developer", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": user_input
        }
    ]
)

# print(completion.choices[0].message)
print(completion.choices[0].message.content)

