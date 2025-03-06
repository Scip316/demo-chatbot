import os
import discord
from openai import OpenAI
from dotenv import load_dotenv
from discord.ext import commands

#Pre-req for the bot
load_dotenv()
bot_token = os.environ.get("Discord_Token")
api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"),
)
intents = discord.Intents.default()  
intents.message_content = True  
conversation_history = {}


#Error handling for tokens
if not bot_token:
    raise ValueError("Error with Discord Bot Token")
if not api_key:
    raise ValueError("Error with API Key")

#Read the prompt file
def load_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

#Reduce history to keep within token
def trim_conversation_history(history, max_messages=3):
    if len(history) > max_messages:
        history = [history[0]] + history[-(max_messages - 1):]
    return history

# Bot prefix
bot = commands.Bot(command_prefix="%", intents=intents)

# Event: Init
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(f'Loading.. Loading.. Loading complete')

# load system instuctions:
prompt = load_text_file("bot_instuctions.txt")

# Bot command
@bot.command()
async def chat(ctx, *, user_input: str):
    try:
        # Get user ID and init the convo
        user_id = ctx.author.id
        if user_id not in conversation_history:
            conversation_history[user_id] = [
                {"role": "system", "content": prompt}
            ]
        conversation_history[user_id].append({"role": "user", "content": user_input})
        conversation_history[user_id] = trim_conversation_history(conversation_history[user_id], max_messages=3)

        print("\nConversation History:")
        for message in conversation_history[user_id]:
            print(f"{message['role']}: {message['content']}")

        # Call the OpenAI API to generate a response
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation_history[user_id],
            max_tokens=600,
        )
        reply = response.choices[0].message.content
        conversation_history[user_id].append({"role": "assistant", "content": reply})
        await ctx.send(reply)

    except Exception as e:
        await ctx.send(f"Who am I.. where am I? oh no no n--- ERROR: {e} \nDamian: Restart the simulation! (Please alert Scip)")

# Error handling
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"Damian: Really? You think you can do your own command? No, use '%chat'. We can do this all day MUHAHAHAHA.")
    else:
        raise error

# Run bot
bot.run(bot_token)