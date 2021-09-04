# emoji_letters.py
import os
import discord
from distutils.util import strtobool
from dotenv import load_dotenv
from collections import Counter

load_dotenv()
client = discord.Client()

emoji_letter_dict = {
    "A": "🇦",
    "B": "🅱️",
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

async def parseMessageAddEmoji(message):
    split_message = message.content.split()
    emoji_word = getLongestWordWithDistinctLetters(split_message)
    if len(emoji_word) >= int(os.getenv('MIN_WORD_LENGTH')) and len(emoji_word) <= int(os.getenv('MAX_WORD_LENGTH')):
        for letter in emoji_word:
            await message.add_reaction(emoji_letter_dict[letter])


async def execute(message):
    await parseMessageAddEmoji(message)