import discord
from discord.ext import commands
import os

TOKEN = os.environ.get('TOKEN')



intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print("Bot is loaded and running.")


bot.run(TOKEN)
