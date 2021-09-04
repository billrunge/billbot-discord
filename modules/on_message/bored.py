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

async def getBoredData():
    url = "https://www.boredapi.com/api/activity/"

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
        if len(data) > 0:
            return data
        else:
            return

async def execute(message):
    word_array = message.content.split()
    if ('BORED' in message.content.upper()):
        data = await getBoredData()
        if data is not None:
            await message.channel.send(f"Bored? You should {data['activity']}")