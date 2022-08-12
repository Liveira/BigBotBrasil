import discord
from discord.ext import commands
import json
import os
from discord.flags import Intents
import requests
import typing
from PIL import Image as img, ImageDraw
from PIL import ImageFont as imgfont
from PIL import ImageDraw as imgdraw
from PIL import ImageOps
import discord,json,asyncio,random,textwrap
from discord.ext import commands,tasks

with open("configuration.json", "r") as config: 
	data = json.load(config)
	token = data["token"]
	owner_id = data["owner_id"]



class Greetings(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self._last_member = None

# Intents
intents = discord.Intents.default()
# The bot
bot = commands.Bot("-", intents = intents, owner_id = owner_id)

# Load cogs
if __name__ == '__main__':
	for filename in os.listdir("Cogs"):
		if filename.endswith(".py"):
			bot.load_extension(f"Cogs.{filename[:-3]}")

@bot.event
async def on_ready():
	print(f"We have logged in as {bot.user}")
	print(discord.__version__)
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"{bot.command_prefix}help"))

bot.run(token)