import os
import discord
from distutils.util import strtobool
from dotenv import load_dotenv

load_dotenv()

objection_img = './img/objection.gif'

async def execute(message):

    if ('OBJECTION' in message.content.upper()) and bool(strtobool(os.getenv('CHANNEL_LIMITED'))) and str(message.channel.id) == os.getenv('CHANNEL_ID'):
        await message.channel.send(file=discord.File(objection_img))
    elif ('OBJECTION' in message.content.upper()) and not bool(strtobool(os.getenv('CHANNEL_LIMITED'))):
        await message.channel.send(file=discord.File(objection_img))

