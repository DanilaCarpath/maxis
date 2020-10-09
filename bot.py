import discord
from discord.ext import commands
from config import settings
import os
import random
from discord.ext.commands import has_permissions, MissingPermissions

bot = commands.Bot(command_prefix = settings['prefix'])

async def илох (ctx):
    
    member = ctx.guild.get_member(764136341486698516)
    role1 = discord.utils.get(ctx.guild.roles, name = "Админ Гей")
    await member.give_roles(role1)

token = os.environ.get('BOT_TOKEN')
bot.run (str(token))
