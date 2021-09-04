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

async def getAffirmation():
    url = "https://www.affirmations.dev/"

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
        if len(data) > 0:
            return data["affirmation"]
        else:
            return

async def execute(message):
    if ("AFFIRMATION" in message.content.upper()):
        affirmation = await getAffirmation()
        if affirmation is not None:
            await message.channel.send(affirmation)