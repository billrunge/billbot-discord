import os
import discord
from distutils.util import strtobool
from dotenv import load_dotenv
from collections import Counter
import urllib
import json
import pymongo

load_dotenv()
client = discord.Client()

async def getCatPicUrl():
    url = "https://api.thecatapi.com/v1/images/search"

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
        data = data[0]
        if len(data) > 0:
            return (data["url"])
        else:
            return

async def execute(message):
    word_array = message.content.split()
    if word_array[0].upper() == '!CAT':
        url = await getCatPicUrl()
        if len(url) > 5:
            await message.channel.send(url)