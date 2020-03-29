import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='%')
TOKEN = "NjkzMzA5NzgxNzk2MDYxMjE0.Xn__3g.oSLf3EqFhg2rD-9v9mGjB_kW0BM"


@bot.event
async def on_ready():
    print("Webdriver Torso, at your service!")
    
@bot.command(name="henlo")
async def henlo(ctx):
    await ctx.send("Hello, World!")
        

bot.run(TOKEN)
