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

async def getSimpsonsData():
    url = "https://thesimpsonsquoteapi.glitch.me/quotes"

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
        data = data[0]
        if len(data) > 0:
            return data
        else:
            return

async def execute(message):
    word_array = message.content.split()
    if word_array[0].upper() == '!SIMPSONS':
        data = await getSimpsonsData()
        if data is not None:
            await message.channel.send(f'{data["image"]} \n' +
                                        f'{data["quote"]} \n' +
                                        f'-{data["quote"]} \n')