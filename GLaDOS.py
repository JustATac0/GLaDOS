#
# Code Written by JustATac0
# "Want you gone" added by Kneeecaps
# original repository: https://github.com/JustATac0/GLaDOS
# just putting that there so I know where to make the pull request if I close the tab
#
#DOWNLOAD LINK FOR "STILL ALIVE": https://github.com/JustATac0/GLaDOS/files/8354516/stillalivemp3.zip
#DOWNLAOD FOR "I WANT YOU GONE": https://vgmsite.com/soundtracks/portal-2-soundtrack-songs-to-test-by-collectors-edition/nuissmiaiv/3-13%20-%20Want%20You%20Gone%20%5BFeat.%20Ellen%20McLain%5D.mp3
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

stillaliveTimes = [
    3,
    4,
    1.5,
    3,
    2,
    4.5,
    4,
    1.5,
    3,
    3,
    2,
    1.8,
    1.8,
    1.8,
    1.8,
    1.8,
    1.5,
    1.5,
    8,
    4,
    4,
    2,
    2,
    3,
    3,
    2.5,
    3,
    3,
    1.8,
    1.8,
    1.8,
    1.8,
    1.8,
    1.5,
    1.8,
    1.2,
    8,
    4,
    4,
    2,
    2,
    3,
    3,
    2,
    2.5,
    1.5,
    2,
    1.8,
    1.8,
    1.8,
    1.8,
    1.8,
    1.5,
    1.8,
    1.2
]
stillaliveLyrics = [
    "This was a triumph.",
    "I'm making a note here:",
    "**HUGE SUCCESS.**",
    "It's hard to overstate",
    "my satisfaction.",
    "Aperture Science",
    "We do what we must",
    "because we can.",
    "For the good of all of us.",
    "Except the ones who are dead.",
    "But there's no sense crying",
    "over every mistake.",
    "You just keep on trying",
    "till you run out of cake.",
    "And the Science gets done.",
    "And you make a neat gun.",
    "For the people who are",
    "**still alive.**",
    "I'm not even angry.",
    "I'm being so sincere right now.",
    "Even though you",
    "broke my heart.",
    "And killed me.",
    "And tore me to pieces.",
    "And threw every piece into",
    "a fire.",
    "As they burned it hurt because",
    "I was so happy for you!",
    "Now these points of data",
    "make a beautiful line.",
    "And we're out of beta.",
    "We're releasing on time.",
    "So I'm GLaD. I got burned.",
    "Think of all the things we learned",
    "for the people who are",
    "**still alive.**",
    "Go ahead and leave me.",
    "I think I prefer to stay inside.",
    "Maybe you'll find",
    "someone else",
    "to help you.",
    "Maybe Black Mesa",
    "THAT WAS A JOKE.",
    "** HA HA. FAT CHANCE.**",
    "Anyway,",
    "this cake is great.",
    "It's so delicious and moist.",
    "Look at me still talking",
    "when there's Science to do.",
    "When I look out there,",
    "it makes me GLaD I'm not you.",
    "I've experiments to run.",
    "There is research to be done.",
    "on the people who are",
    "**still alive.**",
    "And believe me I am",
    "**still alive.**",
    "I'm doing Science and I'm",
    "**still alive.**",
    "I feel FANTASTIC and I'm",
    "**still alive.**",
    "While you're dying I'll be",
    "**still alive.**",
    "And when you're dead I will be",
    "**still alive.**",
    "**STILL ALIVE**",
    "**still alive.**"
]

wantyougoneTimes = [
    5,
    1,
    2,
    1,
    2,
    1.5,
    2,
    1.5,
    3.2,
    1.5,
    2,
    4,
    2.3,
    .05,
    6.8,
    1.6,
    1.4,
    3.5,
    1.8,
    1.8,
    .8,
    3.8,
    .3,
    .6,
    2,
    4,
    2,
    7.5,
    1.5,
    1.5,
    1.5,
    2.5,
    1.5,
    1.5,
    1.5,
    2.6,
    3.7,
    4.4,
    2.7,
    4,
    4
]

wantyougoneLyrics = [
    "Well here we are again",
    "It's always such a pleasure",
    "Remember when you tried",
    "to kill me twice?",
    "Oh how we laughed and laughed",
    "Except I wasn't laughing",
    "Under the circumstances",
    "I've been shockingly nice",
    "You want your freedom?",
    "Take it",
    "That's what I'm counting on",
    "I used to want you dead",
    "But",
    "now I only want you gone",
    "She was a lot like you",
    "(Maybe not quite as heavy)",
    "Now little Caroline is in here too",
    "One day they woke me up",
    "So I could live forever",
    "It's such a shame the same",
    "Will never happen to you",
    "You've got your",
    "short sad",
    "life left",
    "That's what I'm counting on",
    "I'll let you get right to it",
    "Now I only want you gone",
    "Goodbye my only friend",
    "Oh, did you think I meant you?",
    "That would be funny",
    "if it weren't so sad",
    "Well you have been replaced",
    "I don't need anyone now",
    "When I delete you maybe",
    "[REDACTED]",
    "Go make some new disaster",
    "That's what I'm counting on",
    "You're someone else's problem",
    "Now I only want you gone",
    "Now I only want you gone",
    "Now I only want you gone"
]

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
        await asyncio.sleep(stillaliveTimes[0])
        await ctx.send(stillaliveLyrics[0])
        await voice.move_to(channel)
        source = FFmpegPCMAudio('stillalive.mp3')
        player = voice.play(source)

        for i in range(1, len(stillaliveLyrics)):
            async with ctx.typing():
                await asyncio.sleep(stillaliveTimes[i])
            await ctx.send(stillaliveLyrics[i])

@client.command()
async def wantyougone(ctx):
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
        await voice.move_to(channel)
        source = FFmpegPCMAudio('wantyougone.mp3')
        player = voice.play(source)

        for i in range(0, len(wantyougoneLyrics)):
            async with ctx.typing():
                await asyncio.sleep(wantyougoneTimes[i])
            await ctx.send(wantyougoneLyrics[i])

@client.command(pass_context=True)
async def purge(ctx, amount=30):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount + 1):
              messages.append(message)

    await channel.delete_messages(messages)


client.run(TOKEN)
