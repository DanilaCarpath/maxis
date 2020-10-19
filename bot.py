import discord
from discord.ext import commands
from config import settings
import os
import random
from discord.ext.commands import has_permissions, MissingPermissions
import requests
import discord
from discord import Webhook, RequestsWebhookAdapter, File

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.event 
async def on_message(message):
      
	
 
	# Create webhook
	webhook = Webhook.partial(767711039767707661, NfQYdqQspoK-_Xe3VVjiCnx1JNeO1EMX_TOOci37ATskQ7Z40KB_UfUhjorjKWrN5Skm)

	webhook.send("ddsfdfg")
          
    
#         avatar = message.author.avatar_url
#         messageAuthorTemp = '{0.author}'.format(message)
#         messageAuthor = messageAuthorTemp[:-5]
          
#         #поиск канала international
#         tempguild = message.guild
#         channel = discord.utils.get (tempguild.channels, name = "international")
    
    
    

        
token = os.environ.get('BOT_TOKEN')
bot.run (str(token))
