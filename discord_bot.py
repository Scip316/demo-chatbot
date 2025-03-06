import os
import discord
from openai import OpenAI
from dotenv import load_dotenv
from discord.ext import commands

#Pre-req for the bot
load_dotenv()
bot_token = os.environ.get("Test_Bot_Token"),
client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"),
)

#Error for tokens
if not bot_token:
    raise ValueError("Error with Discord Bot Token")
if not api_key:
    raise ValueError("Error with API Key")

# Bot prefix
bot = commands.Bot(command_prefix="%")

# Event: When the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command: Respond to !hello
@bot.command()
async def hello(ctx):
    await ctx.send("Hello, world!")

# Run the bot with your token
bot.run(bot_token)
