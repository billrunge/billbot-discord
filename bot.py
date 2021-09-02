# bot.py
import os

import discord
from dotenv import load_dotenv
from collections import Counter

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL = os.getenv('DISCORD_CHANNEL_ID')

client = discord.Client()

intents = discord.Intents.none()
intents.reactions = True
intents.members = True
intents.guilds = True

emoji_letters = {
    "A": "🇦",
    "B": "🇧",
    "C": "🇨",
    "D": "🇩",
    "E": "🇪",
    "F": "🇫",
    "G": "🇬",
    "H": "🇭",
    "I": "🇮",
    "J": "🇯",
    "K": "🇰",
    "L": "🇱",
    "M": "🇲",
    "N": "🇳",
    "O": "🇴",
    "P": "🇵",
    "Q": "🇶",
    "R": "🇷",
    "S": "🇸",
    "T": "🇹",
    "U": "🇺",
    "V": "🇻",
    "W": "🇼",
    "X": "🇽",
    "Y": "🇾",
    "Z": "🇿"
}


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


@client.event
async def on_message(message):
    if str(message.channel.id) == CHANNEL:
        split_message = message.content.split()
        emoji_word = getLongestWordWithDistinctLetters(split_message)
        if len(emoji_word) > 4 and len(emoji_word) < 21:
            for letter in emoji_word:
                await message.add_reaction(emoji_letters[letter])

client.run(TOKEN)