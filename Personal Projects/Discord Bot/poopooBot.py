import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')
GUILD=os.getenv('GUILD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(bot.user.name, 'has connected to the server!')

@bot.command(name='response', help='Responds with a random response, drawn from a list.')
async def randomResponse(ctx):
    randomResponses=[
        'peepee',\
        'poopoo',\
        'According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don\'t care what humans think is impossible.',\
        'me when the when the',\
        'HELP I\'M TRAPPED INSIDE A DISCORD BOT'\
    ]
    response=random.choice(randomResponses)
    await ctx.send(response)

@bot.command(name='f', help='Pays Respects')
async def payRespects(ctx):
    response='Oof sorry bout that my dude it looks like you done gone died. RIP.'
    await ctx.send(response)

bot.run(TOKEN)