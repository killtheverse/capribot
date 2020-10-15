import discord
import os
from discord.ext import commands
from music import Music

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def pic(channel, file):
    filename = 'images/'+file+'.jpeg'
    await channel.send(file=discord.File(filename))
    
@client.command(pass_context=True)
async def stop_radio(context):
    await leave_voice(context)

@client.command()
async def join_voice(context):
    connected = context.author.voice
    if connected:
        return await connected.channel.connect()

@client.command()
async def leave_voice(context):
    if connected := context.guild.voice_client:
        return await connected.disconnect()
    else:
        return await context.send("Not connected to any voice channel...")
        
    # return await context.send("I am not connected to any voice channel..")
        
token = os.environ['discord_token']

client.add_cog(Music(client))

client.run(token)