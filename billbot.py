import os
import discord
from discord import channel
from modules.on_message import * 
from dotenv import load_dotenv
from importlib.machinery import SourceFileLoader
from database import get_database

load_dotenv()
client = discord.Client()
dbname = get_database()

async def billbotExecute(message, all_modules, channel_modules):

    if ('FEATURES' in message.content.upper()):
        for module in all_modules.find():
            module_name = module["name"].rstrip('.py')
            for channel_module in channel_modules.find():
                if module_name == channel_module["module_name"]:
                    module_name += ': Enabled'
            await message.channel.send(module_name)
    if ('ENABLE'in message.content.upper()):
        word_array = message.content.split()
        for word in word_array:
            for module in all_modules.find():
                module_name = module["name"].rstrip('.py')
                if (word.upper() == module_name.upper()):
                    channel_modules.replace_one({'module_name': module_name, 'channel_id':  message.channel.id},
                    {'module_name': module_name, 'channel_id':  message.channel.id}, upsert = True) 
    if ('DISABLE'in message.content.upper()):
        word_array = message.content.split()
        for word in word_array:
            for module in all_modules.find():
                module_name = module["name"].rstrip('.py')
                if (word.upper() == module_name.upper()):
                    channel_modules.delete_one({'module_name': module_name, 'channel_id':  message.channel.id})