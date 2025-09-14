import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")  # Token will come from Railway's variables

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("pong 🏓")

bot.run(TOKEN)
