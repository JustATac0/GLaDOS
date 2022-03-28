#
# Code Written by JustATac0
# "Want you gone" added by Kneeecaps
# additional optimizations by Oman395
# original repository: https://github.com/JustATac0/GLaDOS
# just putting that there so I know where to make the pull request if I close the tab
#
# DOWNLOAD LINK FOR "STILL ALIVE": https://github.com/JustATac0/GLaDOS/files/8354516/stillalivemp3.zip
# DOWNLAOD FOR "I WANT YOU GONE": https://vgmsite.com/soundtracks/portal-2-soundtrack-songs-to-test-by-collectors-edition/nuissmiaiv/3-13%20-%20Want%20You%20Gone%20%5BFeat.%20Ellen%20McLain%5D.mp3
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

stillaliveLyrics = [
    [0, "This was a triumph."],
    [4, "I'm making a note here:"],
    [1.5, "**HUGE SUCCESS.**"],
    [3, "It's hard to overstate"],
    [2, "my satisfaction."],
    [4.5, "Aperture Science"],
    [4, "We do what we must"],
    [1.5, "because we can."],
    [3, "For the good of all of us."],
    [3, "Except the ones who are dead."],
    [2, "But there's no sense crying"],
    [1.8, "over every mistake."],
    [1.8, "You just keep on trying"],
    [1.8, "till you run out of cake."],
    [1.8, "And the Science gets done."],
    [1.8, "And you make a neat gun."],
    [1.5, "For the people who are"],
    [1.5, "**still alive.**"],
    [8, "I'm not even angry."],
    [4, "I'm being so sincere right now."],
    [4, "Even though you"],
    [2, "broke my heart."],
    [2, "And killed me."],
    [3, "And tore me to pieces."],
    [3, "And threw every piece into"],
    [2.5, "a fire."],
    [3, "As they burned it hurt because"],
    [3, "I was so happy for you!"],
    [1.8, "Now these points of data"],
    [1.8, "make a beautiful line."],
    [1.8, "And we're out of beta."],
    [1.8, "We're releasing on time."],
    [1.8, "So I'm GLaD. I got burned."],
    [1.5, "Think of all the things we learned"],
    [1.8, "for the people who are"],
    [1.2, "**still alive.**"],
    [8, "Go ahead and leave me."],
    [4, "I think I prefer to stay inside."],
    [4, "Maybe you'll find"],
    [2, "someone else"],
    [2, "to help you."],
    [3, "Maybe Black Mesa"],
    [3, "THAT WAS A JOKE."],
    [2, "** HA HA. FAT CHANCE.**"],
    [2.5, "Anyway,"],
    [1.5, "this cake is great."],
    [2, "It's so delicious and moist."],
    [1.8, "Look at me still talking"],
    [1.8, "when there's Science to do."],
    [1.8, "When I look out there,"],
    [1.8, "it makes me GLaD I'm not you."],
    [1.8, "I've experiments to run."],
    [1.5, "There is research to be done."],
    [1.8, "on the people who are"],
    [1.2, "**still alive.**"],
    [1.2, "And believe me I am"],
    [1.2, "**still alive.**"],
    [1.2, "I'm doing Science and I'm"],
    [1.2, "**still alive.**"],
    [1.2, "I feel FANTASTIC and I'm"],
    [1.2, "**still alive.**"],
    [1.2, "While you're dying I'll be"],
    [1.2, "**still alive.**"],
    [1.2, "And when you're dead I will be"],
    [1.2, "**still alive.**"],
    [1.2, "**STILL ALIVE**"],
    [1.2, "**still alive.**"]
]


wantyougoneLyrics = [
    [5, "Well here we are again"],
    [1, "It's always such a pleasure"],
    [2, "Remember when you tried"],
    [1, "to kill me twice?"],
    [2, "Oh how we laughed and laughed"],
    [1.5, "Except I wasn't laughing"],
    [2, "Under the circumstances"],
    [1.5, "I've been shockingly nice"],
    [3.2, "You want your freedom?"],
    [1.5, "Take it"],
    [2, "That's what I'm counting on"],
    [4, "I used to want you dead"],
    [2.3, "But"],
    [.05, "now I only want you gone"],
    [6.8, "She was a lot like you"],
    [1.6, "(Maybe not quite as heavy)"],
    [1.4, "Now little Caroline is in here too"],
    [3.5, "One day they woke me up"],
    [1.8, "So I could live forever"],
    [1.8, "It's such a shame the same"],
    [.8, "Will never happen to you"],
    [3.8, "You've got your"],
    [.3, "short sad"],
    [.6, "life left"],
    [2, "That's what I'm counting on"],
    [4, "I'll let you get right to it"],
    [2, "Now I only want you gone"],
    [7.5, "Goodbye my only friend"],
    [1.5, "Oh, did you think I meant you?"],
    [1.5, "That would be funny"],
    [1.5, "if it weren't so sad"],
    [2.5, "Well you have been replaced"],
    [1.5, "I don't need anyone now"],
    [1.5, "When I delete you maybe"],
    [1.5, "[REDACTED]"],
    [2.6, "Go make some new disaster"],
    [3.7, "That's what I'm counting on"],
    [4.4, "You're someone else's problem"],
    [2.7, "Now I only want you gone"],
    [4, "Now I only want you gone"],
    [4, "Now I only want you gone"]
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
        await voice.move_to(channel)
        source = FFmpegPCMAudio('stillalive.mp3')
        player = voice.play(source)

        for i in stillaliveLyrics:
            async with ctx.typing():
                await asyncio.sleep(i[0])
            await ctx.send(i[1])

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

        for i in wantyougoneLyrics:
            async with ctx.typing():
                await asyncio.sleep(i[0])
            await ctx.send(i[1])

@client.command(pass_context=True)
async def purge(ctx, amount=30):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount + 1):
              messages.append(message)

    await channel.delete_messages(messages)


client.run(TOKEN)
