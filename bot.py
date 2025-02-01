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

# V.1 REGEX TWITTER_URL_REGEX = re.compile(r"(https?:\/\/)?(www\.)?(?:x\.com|xcancel\.com|twitter\.com|fxtwitter\.com|vxtwitter\.com)\/([\w/?=&%-]+)")

# V.2 REGEX
TWITTER_URL_REGEX = re.compile(r"(https?:\/\/)?(www\.)?(?:x\.com|xcancel\.com|twitter\.com|fxtwitter\.com|vxtwitter\.com)\/([^\s]+)")

@bot.event
async def on_ready():
    print(f"Bot has logged in as {bot.user}")

@bot.event
async def on_message(message):
    BASE_URL = "https://vxtwitter.com/"

    if message.author == bot.user:
        return
    
    match = TWITTER_URL_REGEX.search(message.content)
    if match:
        if match.group(3) is None:
            print("Error Parsing URL")
            return
        
        info = match.group(3)
        info = info.split("?")[0]
        # if check_embed_type(message):
            
        if not check_embed_type(message):
            print("Not Vid Embed")
            BASE_URL = "https://xcancel.com/"

        
        new_url = f"{BASE_URL}{info}"

        modified_message = TWITTER_URL_REGEX.sub(new_url, message.content)
        
        await message.channel.send(f"{message.author.mention} shared: {modified_message}")
        
        await message.delete()

def check_embed_type(message):
    for embed in message.embeds:
        if embed.video or embed.image:
            return True

    return False


bot.run(BOT_TOKEN)