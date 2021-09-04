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
            modules = ''
            module_name = module["name"].rstrip('.py')
            for channel_module in channel_modules.find({'channel_id':  message.channel.id}):
                if module_name == channel_module["module_name"]:
                    module_name += ': enabled'
            modules += f'{module_name} \n'
        await message.channel.send(modules)
    if ('ENABLE' in message.content.upper()):
        word_array = message.content.split()
        for word in word_array:
            for module in all_modules.find():
                module_name = module["name"].rstrip('.py')
                if (word.upper() == module_name.upper()):
                    channel_modules.replace_one({'module_name': module_name, 'channel_id':  message.channel.id},
                                                {'module_name': module_name, 'channel_id':  message.channel.id}, upsert=True)
    if ('DISABLE' in message.content.upper()):
        word_array = message.content.split()
        for word in word_array:
            for module in all_modules.find():
                module_name = module["name"].rstrip('.py')
                if (word.upper() == module_name.upper()):
                    channel_modules.delete_one(
                        {'module_name': module_name, 'channel_id':  message.channel.id})
    if ('HELP' in message.content.upper()):

        await message.channel.send('Thank you for using Billbot \n' +
                                    'To see all features available and their enabled status: \n' +
                                    '`!BILLBOT features`\n' +
                                    'To enable a feature for the current channel: \n' +
                                    '`!BILLBOT enable <feature name>` \n' +
                                    'To disable a feature for the current channel: \n' +
                                    '`!BILLBOT disable <feature name>`')


