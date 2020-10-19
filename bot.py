import discord
from discord.ext import commands
from config import settings
import os
import random
from discord.ext.commands import has_permissions, MissingPermissions

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.event
async def on_message(message):
    
    if message.author.bot:
        print ("bot")
    else:
        
        avatar = message.author.avatar_url
        messageAuthorTemp = '{0.author}'.format(message)
        messageAuthor = messageAuthorTemp[:-5]

        #поиск канала international
        tempguild = message.guild
        channel = discord.utils.get (tempguild.channels, name = "international")

        #создание эмбеда
        embed = discord.Embed (color=0x6600ff, description = message.content )
        embed.set_author (name = messageAuthor, icon_url = avatar)

        webhook = discord.Webhook ("767711039767707661", "NfQYdqQspoK-_Xe3VVjiCnx1JNeO1EMX_TOOci37ATskQ7Z40KB_UfUhjorjKWrN5Skm")
        webhook.send (message.content)

token = os.environ.get('BOT_TOKEN')
bot.run (str(token))
