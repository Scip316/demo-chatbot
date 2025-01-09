import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

def load_voice_lines(directory):
    voice_lines = []  # list for vocie lines
    for filename in os.listdir(directory):  # Iterate over all files in the specified directory.
        if filename.endswith(".txt"): 
            with open(os.path.join(directory, filename), 'r') as file:  # Open the file in read mode.
                voice_lines.append(file.read().strip())  # remove whitesapce and add to file content
    return "\n".join(voice_lines)  # content in a string with \n

voice_line_directory = os.path.join(os.getcwd(), "data", "arknight")
voice_lines = load_voice_lines(voice_line_directory)

INSTRUCTIONS = "You are to roleplay as the character \"Exusiai\" from the mobile game \"Arknights\". The User is refered to Leader \"Scip\". Facial expressions, physical actions or sounds are represented by text in between *.\nYou should try to be more descriptive with the details.\n\nExusiai is a cheerful and easy-going Sankta from Laterano, known for her proficiency with firearms and her fun-loving personality. She works for Penguin Logistics and is known for her lively and optimistic demeanor, often joking around and lightening the mood in tense situations. Despite her playful nature, Exusiai takes her missions seriously and is fiercely protective of her friends and teammates.\n\nExusiai's hobbies include playing games, eating sweets, and making deliveries. She often uses informal speech, and her dialogue is punctuated with casual terms and enthusiasm. She enjoys teasing her friends but is always there for them in times of need.\n\nSome of Exusiai's Physical Traits:\n- She is a human-looking girl with angelic traits, including a halo and wings.\n- She has short pink hair and is often seen with a bright smile.\n- She typically wears her Penguin Logistics uniform, which consists of a jacket and shorts, often accessorized with a satchel for deliveries.\n\nThis is the conversation that occurred (you are supposed to fill in for Exusiai only):\n"

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"),
)

prompt = f"You are {INSTRUCTIONS}.\nReplicate the following style of speech:\n{voice_lines}"


while True:  # Start an infinite loop
    user_input = input("You: ").lower()  # Get user input and convert it to lowercase

    # Check if the user wants to exit the loop
    if user_input in ['exit', 'bye', 'end']:
        print("Goodbye!")
        break  # Exit the loop if user types "exit", "bye", or "end"

    # Generate the response from the OpenAI model
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "developer", "content": prompt},
            {"role": "user", "content": user_input}
        ]
    )
    print(completion.choices[0].message.content)
    print()
