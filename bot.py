# bot.py
import os
import discord
from discord import channel
from modules.on_message import *
from dotenv import load_dotenv
from importlib.machinery import SourceFileLoader
from database import get_database
from billbot import billbotExecute

load_dotenv()
client = discord.Client()
dbname = get_database()


def loadModules():
    all_modules_db = dbname["all_modules"]
    all_modules_db.delete_many({})

    modules_dir = os.listdir("modules")
    for dir in modules_dir:
        print(dir)
        list_modules = os.listdir(f'modules/{dir}')
        list_modules.remove('__init__.py')
        for module_name in list_modules:
            if module_name.split('.')[-1] == 'py':
                all_modules_db.insert_one({"name": module_name, "type": dir})

# if os.getenv('bop') == None:
#     print("test")


loadModules()


@client.event
async def on_message(message):
    all_modules = dbname["all_modules"]
    channel_modules = dbname["channel_modules"]

    if (str(message.content[0:8]).upper() == '!BILLBOT'):
        await billbotExecute(message, all_modules, channel_modules)
    for module_object in all_modules.find():
        module_name = module_object["name"]
        type = module_object["type"]
        if type == 'on_message' and channel_modules.find_one({'module_name': module_name.rstrip('.py'), 'channel_id':  message.channel.id}) is not None:
            module = SourceFileLoader(
                module_name, f'modules/{type}/{module_name}').load_module()
            await module.execute(message)

client.run(os.getenv('TOKEN'))
