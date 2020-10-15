import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def pic(channel, file):
    filename = 'images/'+file+'.jpeg'
    await channel.send(file=discord.File(filename))
    
@client.command()
async def homie(channel):
    await channel.send(file=discord.File('images/homie.jpeg'))
    
@client.command()
async def lofi(context):
    voice_channel = await join_voice(context)
    voice_channel.play(discord.FFmpegOpusAudio("https://www.youtube.com/watch?v=5qap5aO4i9A"))

@client.command()
async def nightwave(context):
    voice_channel = await join_voice(context)
    voice_channel.play(discord.FFmpegOpusAudio("http://radio.plaza.one/opus"))

@client.command(pass_context=True)
async def stop(context):
    await leave_voice(context)

@commands.command()
async def join_voice(context):
    connected = context.author.voice
    if connected:
        return await connected.channel.connect()

@commands.command()
async def leave_voice(context):
    if connected := context.guild.voice_client:
        return await connected.disconnect()
    else:
        return await context.send("Not connected to any voice channel...")
        
    # return await context.send("I am not connected to any voice channel..")
        
token = os.environ['discord_token']
# from config import token
client.run(token)