from dotenv import load_dotenv
from openai import OpenAI
from character import *

load_dotenv()

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"),
)

prompt = character_section()

while True: 
    user_input = input("You: ").lower()  
    if user_input in ['exit', 'bye', 'end']:
        print("System: Exiting...")
        break 
    # Generate the response from the OpenAI model
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_input}
        ]
    )
    print(completion.choices[0].message.content)
    print()