import discord
import dotenv

import re
import os

from discord.ext import commands

dotenv.load_dotenv()

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
TARGET_CHANNEL_ID = os.environ.get('TARGET_CHANNEL_ID', None) 

client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix="!", intents=intents)

TWITTER_URL_REGEX = re.compile(r"(https?:\/\/)?(www\.)?x\.com\/([\w/?=&%-]+)")

@bot.event
async def on_ready():
    print(f"Bot have logged in as {bot.user}")

@bot.event
async def on_message(message):
    BASE_URL = "https://vxtwitter.com/"

    if message.author == bot.user:
        return
    
    match = TWITTER_URL_REGEX.search(message.content)
    if match:
        if match.group(3) is None:
            await message.channel.send("Error parsing X Url")
            
        info = match.group(3)
        
        # if check_embed_type(message):
            
        new_url = f"{BASE_URL}{info}"
        
        await message.channel.send(f"{message.author.mention} Posted this link from X: {new_url}")
        
        await message.delete()

def check_embed_type(message):
    for embed in message.embeds:
        if embed.video or embed.image:
            return True

    return False


bot.run(BOT_TOKEN)