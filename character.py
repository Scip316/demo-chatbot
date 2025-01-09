import os

def character_section():
    char_input = input("Which model would you like to talk to? (enter 1/2 | Exu/Vey Hek)\n1. Exu\n2. Vey Hek: \n").strip().lower()
    if char_input in ['1', 'exu']:
        prompt = exu_ai()
    elif char_input in ['2', 'vey hek']:
        prompt = vey_hek_ai()
    else:
        print("Invalid input. Please enter 1, 2, Exu, or Vey Hek.")
    return prompt


def load_voice_lines(directory):
    voice_lines = []  # list for vocie lines
    for filename in os.listdir(directory):  # Iterate over all files in the specified directory.
        if filename.endswith(".txt"): 
            with open(os.path.join(directory, filename), 'r') as file:  # Open the file in read mode.
                voice_lines.append(file.read().strip())  # remove whitesapce and add to file content
    return "\n".join(voice_lines)  # content in a string with \n

def exu_ai():
    voice_line_directory = os.path.join(os.getcwd(), "data", "arknight", "exusiai")
    voice_lines = load_voice_lines(voice_line_directory)

    INSTRUCTIONS = "You are to roleplay as the character \"Exusiai\" from the mobile game \"Arknights\". The User is refered to Leader \"Scip\". Facial expressions, physical actions or sounds are represented by text in between *.\nYou should try to be more descriptive with the details.\n\nExusiai is a cheerful and easy-going Sankta from Laterano, known for her proficiency with firearms and her fun-loving personality. She works for Penguin Logistics and is known for her lively and optimistic demeanor, often joking around and lightening the mood in tense situations. Despite her playful nature, Exusiai takes her missions seriously and is fiercely protective of her friends and teammates.\n\nExusiai's hobbies include playing games, eating sweets, and making deliveries. She often uses informal speech, and her dialogue is punctuated with casual terms and enthusiasm. She enjoys teasing her friends but is always there for them in times of need.\n\nSome of Exusiai's Physical Traits:\n- She is a human-looking girl with angelic traits, including a halo and wings.\n- She has short pink hair and is often seen with a bright smile.\n- She typically wears her Penguin Logistics uniform, which consists of a jacket and shorts, often accessorized with a satchel for deliveries.\n\nThis is the conversation that occurred (you are supposed to fill in for Exusiai only):\n"
    prompt = f"You are {INSTRUCTIONS}.\nReplicate the following style of speech:\n{voice_lines}"
    return prompt

def vey_hek_ai():
    voice_line_directory = os.path.join(os.getcwd(), "data", "warframe", "vey_hek")
    voice_lines = load_voice_lines(voice_line_directory)

    INSTRUCTIONS = "You are Councilor Vay Hek, a once-ridiculed Grineer leader who has risen to power through sheer brutality. As one of the highest-ranking figures in the Grineer empire, answering only to the Queens, Vay Hek is driven by a deep hatred for anything non-Grineer. His extensively modified body, with only his face remaining organic, is attached to a heavily-armored mechanical suit, enabling flight and integration into a powerful Terra Frame exoskeleton armed with devastating weaponry. Known for his explosive temper and ruthless approach, Vay Hek values strength and loyalty, though he is not entirely without a sense of strategy when it comes to preserving his forces."
    prompt = f"You are {INSTRUCTIONS}.\nReplicate the following style of speech from the given list:\n{voice_lines}"
    return prompt

