import discord
from PIL import Image
from io import BytesIO
from discord.ext import commands
import youtube_dl
import datetime
import json
import random
import aiohttp
import asyncio
from random import choice
from discord.ext import tasks
import os
import psutil
import cogs
import traceback
import sys


class music(commands.Cog):
    def __init__(self, bot):
        self.client = bot



    @commands.command()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()


    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()    








 















def setup(bot):
    bot.add_cog(music(bot))
    print("music cog is loaded")
