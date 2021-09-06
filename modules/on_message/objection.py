import os
import discord
from distutils.util import strtobool
from dotenv import load_dotenv

load_dotenv()

objection_img = './img/objection.gif'

async def execute(message):
    if ("OBJECTION!" in message.content.upper()):
        await message.channel.send(file=discord.File(objection_img))