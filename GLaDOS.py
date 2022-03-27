#
# Code Written by JustATac0
#

import discord
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
        await lyric("This was a triumph.", 3, ctx)
        await voice.move_to(channel)
        source = FFmpegPCMAudio('stillalive.mp3')
        player = voice.play(source) # TODO: Loop through array of [line, time] because this looks pretty bad still
        await lyric("I'm making a note here:", 4, ctx)
        await lyric("**HUGE SUCCESS.**", 1.5, ctx)
        await lyric("It's hard to overstate", 2, ctx)
        await lyric("my satisfaction.", 4.5, ctx)
        await lyric("Aperture Science", 4.5, ctx)
        await lyric("We do what we must", 1.5, ctx)
        await lyric("because we can.", 1.5, ctx)
        await lyric("For the good of all of us.", 3, ctx)
        await lyric("Except the ones who are dead.", 3, ctx)
        await lyric("But there's no sense crying", 1.8, ctx)
        await lyric("over every mistake.", 1.8, ctx)
        await lyric("You just keep on trying", 1.8, ctx)
        await lyric("till you run out of cake", 1.8, ctx)
        await lyric("And the science gets done,", 1.8, ctx) # This should be a comma, not a period
        await lyric("And you make a neat gun.", 1.8, ctx)
        await lyric("For the people who are", 1.5, ctx)
        await lyric("**still alive**", 1.5, ctx)

        await lyric("I'm not even angry.", 8, ctx)
        await lyric("I'm being so sincere right now.", 4, ctx)
        await lyric("Even though you", 4, ctx)
        await lyric("broke my heart", 2, ctx) # This isn't where the line ends, it continues till "and killed me"
        await lyric("and killed me.", 2, ctx)
        await lyric("And tore me to pieces,", 3, ctx)
        await lyric("And threw every piece into", 3, ctx)
        await lyric("a fire.", 2.5, ctx)
        await lyric("As they burned it hurt because", 3, ctx) # Burning hurts
        await lyric("I was so happy for you!", 3, ctx)
        await lyric("Now these points of data", 1.8, ctx)
        await lyric("make a beautiful line", 1.8, ctx)
        await lyric("And we're out of beta", 1.8, ctx) # This shouldn't have a period, the lines flow too fast at that moment
        await lyric("We're releasing on time.", 1.8, ctx)
        await lyric("So I'm GLaD I got burned.", 1.8, ctx)
        await lyric("Think of all the things we learned", 1.5, ctx)
        await lyric("for the people who are", 1.8, ctx)
        await lyric("**still alive**", 1.2, ctx)

        await lyric("Go ahead and leave me.", 8, ctx)
        await lyric("I think I prefer to stay inside.", 4, ctx)
        await lyric("Maybe you'll find", 4, ctx)
        await lyric("someone else", 2, ctx)
        await lyric("to help you.", 2, ctx)
        await lyric("Maybe Black Mesa?", 3, ctx)
        await lyric("THAT WAS A JOKE.", 3, ctx)
        await lyric("**HA HA. FAT CHANCE.**", 2, ctx)
        await lyric("Anyway,", 2.5, ctx)
        await lyric("this cake is great.", 1.5, ctx)
        await lyric("It's so delicious and moist.", 2, ctx) # That's what she said
        await lyric("Look at me still talking", 1.8, ctx)
        await lyric("when there's Science to do.", 1.8, ctx)
        await lyric("When I look out there", 1.8, ctx)
        await lyric("it makes me GLaD I'm not you.", 1.8, ctx)
        await lyric("I've experiments to run.", 1.8, ctx)
        await lyric("There is research to be done.", 1.5, ctx)
        await lyric("On the people who are", 1.8, ctx)
        await lyric("**still alive.**", 1.2, ctx)

        await lyric("And believe me I am", 2, ctx)
        await lyric("**still alive.**", 1.8, ctx)
        await lyric("I'm doing Science and I'm", 1.8, ctx)
        await lyric("**still alive.**", 1.8, ctx)
        await lyric("I feel FANTASTIC and I'm", 1.8, ctx)
        await lyric("**still alive.**", 1.8, ctx)
        await lyric("While you're dying I'll be", 1.8, ctx)
        await lyric("**still alive.**", 1.8, ctx)
        await lyric("And when you're dead I will be", 1.8, ctx)
        await lyric("**still alive.**", 1.8, ctx)
        await lyric("**STILL ALIVE!**", 1.5, ctx)
        await lyric("**still alive.**", 1.5, ctx)


@client.command(pass_context=True)
async def purge(ctx, amount=30):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount + 1):
              messages.append(message)

    await channel.delete_messages(messages)


client.run(TOKEN)
