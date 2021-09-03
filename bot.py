# bot.py
import os
import discord
from on_message import *
from dotenv import load_dotenv
from importlib.machinery import SourceFileLoader

load_dotenv()
client = discord.Client()


@client.event
async def on_message(message):

    list_modules=os.listdir('on_message')
    list_modules.remove('__init__.py')
    for module_name in list_modules:
        if module_name.split('.')[-1]=='py':
            foo = SourceFileLoader(module_name, f'on_message/{module_name}').load_module()
            await foo.execute(message)

client.run(os.getenv('TOKEN'))
