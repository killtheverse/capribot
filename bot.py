import discord
import os
from discord.ext import commands
from music import Music

client = commands.Bot(command_prefix='chapri ')

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def pic(channel, file):
    filename = 'images/'+file+'.jpeg'
    await channel.send(file=discord.File(filename))
    
        
token = os.environ['discord_token']

client.add_cog(Music(client))

client.run(token)