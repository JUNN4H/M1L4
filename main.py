import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!. I am programed for doing math thing')

@bot.command()
async def heh(ctx, count_heh = 1000):
    await ctx.send("he" * count_heh)
    
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
    
@bot.command()
async def minus(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left - right)
    
@bot.command()
async def time(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left * right)
    
@bot.command()
async def divide(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left / right)



bot.run(Your Token)
