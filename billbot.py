# import os
# import discord
# from discord.ext import commands
# from dotenv import load_dotenv
# from discord_slash import SlashCommand, SlashContext

# load_dotenv()

# bot = discord.Client(intents=discord.Intents.default())
# slash = SlashCommand(bot)

# @slash.slash(name="test")
# async def test(ctx: SlashContext):
#     embed = discord.Embed(title="Embed Test")
#     await ctx.send(embed=embed)

# bot.run(os.getenv('TOKEN'))