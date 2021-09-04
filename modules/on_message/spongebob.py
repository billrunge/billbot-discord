import os
import discord
from distutils.util import strtobool
from dotenv import load_dotenv

load_dotenv()

img = './img/spongebob.jpg'

async def execute(message):
    word_array = message.content.split()
    output_text = ''
    uppercase = False

    if word_array[0].upper() == '!SPONGEBOB':
        i = 1
        while i < len(word_array):
            word = word_array[i]
            for c in word:
                if uppercase:
                    output_text += c.lower()
                    uppercase = False
                else:
                    output_text += c.upper()
                    uppercase = True
            output_text += ' '
            i += 1

        await message.channel.send(file=discord.File(img))
        await message.channel.send(output_text)