import discord
from discord.ext import commands
from config import settings
import os
import random
from discord.ext.commands import has_permissions, MissingPermissions
from discord_webhook import DiscordWebhook

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.event 
async def on_message(message):
          
    
#         avatar = message.author.avatar_url
#         messageAuthorTemp = '{0.author}'.format(message)
#         messageAuthor = messageAuthorTemp[:-5]
          
#         #поиск канала international
#         tempguild = message.guild
#         channel = discord.utils.get (tempguild.channels, name = "international")
    
    
    webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/767711039767707661/NfQYdqQspoK-_Xe3VVjiCnx1JNeO1EMX_TOOci37ATskQ7Z40KB_UfUhjorjKWrN5Skm', content='fffff')
    webhook.execute()    

        
token = os.environ.get('BOT_TOKEN')
bot.run (str(token))
