import os
import discord
from distutils.util import strtobool
from dotenv import load_dotenv
from collections import Counter
import urllib
import json

load_dotenv()
client = discord.Client()

async def getGifFromGiphy(word):
    url = "http://api.giphy.com/v1/gifs/search"
    params = urllib.parse.urlencode({
        "q": word,
        "api_key": os.getenv('GIPHY_API_KEY'),
        "limit": "1"
    })

    with urllib.request.urlopen(f'{url}?{params}') as response:
        data = json.loads(response.read())
        data = data["data"]
        if len(data) > 0:
            data = data[0]
            return (data["embed_url"])
        else:
            return
        

def isUniqueChars(string):
    freq = Counter(string)
    if(len(freq) == len(string)):
        return True
    else:
        return False

def getLongestWordWithDistinctLetters(word_array):
    longest_length = 0
    longest_word = ''
    for word in word_array:
        word = ''.join(c for c in word if c.isalpha())
        word = word.upper()
        if (len(word) > longest_length and isUniqueChars(word)):
            longest_word = word
            longest_length = len(word)
    return longest_word 


async def parseMessage(message):
    split_message = message.content.split()
    giphy_word = getLongestWordWithDistinctLetters(split_message)

    if len(giphy_word) >= int(os.getenv('MIN_WORD_LENGTH')) and len(giphy_word) <= int(os.getenv('MAX_WORD_LENGTH')):
        gif_url = await getGifFromGiphy(giphy_word)
        if len(gif_url) > 5:
            await message.channel.send(gif_url)

async def execute(message):
    await parseMessage(message)
    # if bool(strtobool(os.getenv('CHANNEL_LIMITED'))) and str(message.channel.id) == os.getenv('CHANNEL_ID'):
    #     await parseMessage(message)
    # elif not bool(strtobool(os.getenv('CHANNEL_LIMITED'))):
    #     await parseMessage(message)



