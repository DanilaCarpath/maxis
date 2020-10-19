import discord
from discord.ext import commands
from config import settings
import os
import random
from discord.ext.commands import has_permissions, MissingPermissions

from discord.utils import get

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.event
async def on_message(message):
    fchannel = bot.get_channel(730634007284285545)
    tchannel = bot.get_channel(765561417842688040)
    webhook_id = 767706987110072340
    hooks = await tchannel.webhooks()
    hook = get(hooks, id=webhook_id)  
    if message.channel == fchannel:
        await hook.send(content=message.content, username=message.author.display_name, 
                        avatar_url=message.author.avatar_url)
    

        
token = os.environ.get('BOT_TOKEN')
bot.run (str(token))
