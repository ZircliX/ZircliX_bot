import discord
from discord.ext import commands
import youtube_dl
import asyncio

bot = commands.Bot(command_prefix = "?", description = "DONUT")
musics = {}
ytdl = youtube_dl.YoutubeDL()

@bot.event
async def on_ready():
    print("Launched !")

class Video:
    def __init__(self, link):
        video = ytdl.extract_info(link, download = False)
        video_format = video["formats"][0]
        self.url = video["webpage_url"]
        self.stream_url = video_format["url"]

def play_song(client, song):
    print("play_song")
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song.stream_url))
    client.play(source)

@bot.command()
async def play(ctx, url):
    print("play")
    client = ctx.guild.voice_client
    print("Connection au channel.")
    channel = ctx.author.voice.channel
    video = Video(url)
    musics[ctx.guild] = []
    client = await channel.connect()
    await ctx.send("Je lance la musique !")
    play_song(client, video)

@bot.command()
async def leave(ctx):
    print("leave")
    client = ctx.guild.voice_client
    await client.disconnect()
    musics[ctx.guild] = []

@bot.command()
async def skip(ctx):
    print("skip")
    client = ctx.guild.voice_client
    client.stop()
    await ctx.send("Suivant !")
    
@bot.command()
async def wsh(ctx): 
    await ctx.send("Wsh poto comment tu vas ?!")

@bot.command()
async def info(ctx):
    server=ctx.guild
    sn=server.name
    np=server.member_count
    await ctx.send(f"Dans **{sn}** il y a **{np}** personnes !")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def oof(ctx):
    await ctx.send("chehhhhh !")

@bot.command()
async def manger(ctx):
    await ctx.send("Bon appétit à toi UwU !")


bot.run("ODMwNzgzOTA5MTE3MTY1NTc4.YHLtzw.6G6c3_MjQ15-xPWqDWtl0mNdC0M")