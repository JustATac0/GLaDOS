#
# Code Written by JustATac0
#

import discord
import json
import time
import asyncio
from discord.ext import commands,tasks
from time import sleep
from discord import FFmpegPCMAudio
from discord.utils import get

client = commands.Bot(command_prefix = ['-', 'GLaD '])
TOKEN = open("gladtoken.txt","r").readline()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Portal"))

@client.command()
async def join(ctx):
    if isinstance(ctx.channel, discord.channel.DMChannel):
        return await ctx.send("Please return to the Aperture Science computer-aided enrichment center.")
    if not ctx.author.voice:
       return await ctx.send("Did you really think that would work if you weren't connected to a voice channel?")
    channel = ctx.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        await channel.connect()
    client_channel = ctx.voice_client.channel
    if channel and channel == client_channel:
        if voice and voice.is_connected():
            await ctx.send("I'm already in the voice channel with you.")

@client.command()
async def leave(ctx):
    if isinstance(ctx.channel, discord.channel.DMChannel):
        return await ctx.send("Please return to the Aperture Science computer-aided enrichment center.")
    if not ctx.message.guild.voice_client:
       return await ctx.send("I'm not currently connected to any voice channels.", delete_after = 5.0)
    await ctx.voice_client.disconnect()

async def  lyric(line, sleep, ctx): # Written by Oman395 for cleaning purposes
    async with ctx.typing():
        await asyncio.sleep(sleep)
    await ctx.send(line)
    return

@client.command()
async def stillalive(ctx):
    if isinstance(ctx.channel, discord.channel.DMChannel):
        return await ctx.send("Please return to the Aperture Science computer-aided enrichment center.")
    if not ctx.author.voice:
        return await ctx.send("Did you really think that would work if you weren't connected to a voice channel?")
    channel = ctx.author.voice.channel
    if not channel:
        return await ctx.send("Did you really think that would work if you weren't connected to a voice channel?")
    voice = get(client.voice_clients, guild=ctx.guild)
    if not voice:
        await ctx.send("Did you really think that would work if I wasn't connected to a voice channel?")
    if voice and voice.is_playing():
        return await ctx.send("Please wait until I am finished before using another voice channel command.")
    if voice and voice.is_connected():
        # From here to end of stillalive() code is cleaned up by Oman395
        await voice.move_to(channel)
        source = FFmpegPCMAudio('stillalive.mp3')
        player = voice.play(source) # TODO: Loop through array of [line, time] because this looks pretty bad still
        
        with open("stillalive.json", 'r') as f:
            data = json.loads(f.read())
        for i in range(len(data)):
            if i == 0:
                await voice.move_to(channel)
                source = FFmpegPCMAudio('stillalive.mp3')
                player = voice.play(source) # TODO: Loop through array of [line, time] because this looks pretty bad still
            await lyric(data[i][0], int(data[i][1]), ctx)

@client.command(pass_context=True)
async def purge(ctx, amount=30):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount + 1):
        messages.append(message)

    await channel.delete_messages(messages)


client.run(TOKEN)
