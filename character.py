import os

def character_section():
    char_input = input("Which model would you like to talk to? (enter 1/2 | Exu/Vey Hek)\n1. Exu\n2. Vey Hek: \n").strip().lower()
    if char_input in ['1', 'exu']:
        prompt = character_prompt("arknight", "exusiai")

    elif char_input in ['2', 'vey hek']:
        prompt = character_prompt("warframe", "vey_hek")
        
    else:
        print("Invalid input. Please enter 1, 2, Exu, or Vey Hek.")
    return prompt

def load_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()


def character_prompt(game, character):
    character_file = os.path.join(os.getcwd(), "data", game, character, "character.txt")
    voice_file = os.path.join(os.getcwd(), "data", game, character, "voice.txt")
    instructions_file = os.path.join(os.getcwd(), "data", game, character, "instructions.txt")
    character_text = load_text_file(character_file)
    voice_lines = load_text_file(voice_file)
    instructions_text = load_text_file(instructions_file)
    prompt = f"""
{character_text}

{voice_lines}

{instructions_text}
    """

    return prompt