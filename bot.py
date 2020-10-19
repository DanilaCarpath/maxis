import discord
from discord.ext import commands
from config import settings
import os
import random
from discord.ext.commands import has_permissions, MissingPermissions

from discord.utils import get

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.command()
async def dm (ctx):
    for member in ctx.guild.members:
        try:
            await member.send ("Внимание! Кекляндия переезжает в Конфу, новую площадку для РП. Для Кекляндии будет отдельный рп уголок, а во время отдыха от рп вы можете поговорить в чате. https://discord.gg/BZ7NQ2m")
        except:
            print ("oshibka")
        
token = os.environ.get('BOT_TOKEN')
bot.run (str(token))
