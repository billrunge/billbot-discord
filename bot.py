# bot.py
import os
import discord
from dotenv import load_dotenv
from collections import Counter
from distutils.util import strtobool
from on_message.emoji_letters import parseMessageAddEmoji
#from on_message.objection import execute

load_dotenv()
client = discord.Client()

@client.event
async def on_message(message):
    # if ('OBJECTION' in message.content.upper()) and bool(strtobool(os.getenv('CHANNEL_LIMITED'))) and str(message.channel.id) == os.getenv('CHANNEL_ID'):
    #     await execute(message)
    # elif ('OBJECTION' in message.content.upper()) and not bool(strtobool(os.getenv('CHANNEL_LIMITED'))):
    #     await execute(message)

    on_message.objection.execute(message)

    if bool(strtobool(os.getenv('CHANNEL_LIMITED'))) and str(message.channel.id) == os.getenv('CHANNEL_ID'):
        await parseMessageAddEmoji(message)
    elif not bool(strtobool(os.getenv('CHANNEL_LIMITED'))):
        await parseMessageAddEmoji(message)


client.run(os.getenv('TOKEN'))
