# bot.py
import os
import discord
from dotenv import load_dotenv
from collections import Counter
from distutils.util import strtobool
from on_message.emoji_letters import parseMessageAddEmoji

load_dotenv()
client = discord.Client()

# emoji_letters = {
#     "A": "🇦",
#     "B": "🅱️",
#     "C": "🇨",
#     "D": "🇩",
#     "E": "🇪",
#     "F": "🇫",
#     "G": "🇬",
#     "H": "🇭",
#     "I": "🇮",
#     "J": "🇯",
#     "K": "🇰",
#     "L": "🇱",
#     "M": "🇲",
#     "N": "🇳",
#     "O": "🇴",
#     "P": "🇵",
#     "Q": "🇶",
#     "R": "🇷",
#     "S": "🇸",
#     "T": "🇹",
#     "U": "🇺",
#     "V": "🇻",
#     "W": "🇼",
#     "X": "🇽",
#     "Y": "🇾",
#     "Z": "🇿"
# }


# def isUniqueChars(string):
#     freq = Counter(string)
#     if(len(freq) == len(string)):
#         return True
#     else:
#         return False


# def getLongestWordWithDistinctLetters(word_array):
#     longest_length = 0
#     longest_word = ''
#     for word in word_array:
#         word = ''.join(c for c in word if c.isalpha())
#         word = word.upper()
#         if (len(word) > longest_length and isUniqueChars(word)):
#             longest_word = word
#             longest_length = len(word)
#     return longest_word


# async def parseMessageAddEmoji(message):
#     split_message = message.content.split()
#     emoji_word = getLongestWordWithDistinctLetters(split_message)
#     if len(emoji_word) >= int(os.getenv('MIN_WORD_LENGTH')) and len(emoji_word) <= int(os.getenv('MAX_WORD_LENGTH')):
#         for letter in emoji_word:
#             await message.add_reaction(emoji_letters[letter])


@client.event
async def on_message(message):
    if ('OBJECTION' in message.content.upper()) and bool(strtobool(os.getenv('CHANNEL_LIMITED'))) and str(message.channel.id) == os.getenv('CHANNEL_ID'):
        await message.channel.send(file=discord.File('img/objection.gif'))
    elif ('OBJECTION' in message.content.upper()) and not bool(strtobool(os.getenv('CHANNEL_LIMITED'))):
        await message.channel.send(file=discord.File('img/objection.gif'))

    if bool(strtobool(os.getenv('CHANNEL_LIMITED'))) and str(message.channel.id) == os.getenv('CHANNEL_ID'):
        await parseMessageAddEmoji(message)
    elif not bool(strtobool(os.getenv('CHANNEL_LIMITED'))):
        await parseMessageAddEmoji(message)


client.run(os.getenv('TOKEN'))
