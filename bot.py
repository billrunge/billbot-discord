# bot.py
import os
import discord
import pymongo
from on_message import * 
from dotenv import load_dotenv
from importlib.machinery import SourceFileLoader

load_dotenv()
client = discord.Client()

# if os.getenv('bop') == None:
#     print("test")

def database():
    dbclient = pymongo.MongoClient(os.getenv('MONGO_DB_CONNECTION_STRING'))
    db = dbclient.test

@client.event
async def on_message(message):

    dir = 'on_message'
    list_modules=os.listdir(dir)
    list_modules.remove('__init__.py')
    for module_name in list_modules:
        if module_name.split('.')[-1]=='py':
            module = SourceFileLoader(module_name, f'{dir}/{module_name}').load_module()
            await module.execute(message)

client.run(os.getenv('TOKEN'))
