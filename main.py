# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import discord
import os
from discord.ext import commands
#from os import system
#from discord.ext import commands
from keep_alive import keep_alive
#from google_images_download import google_images_download
import random
#from bs4 import BeautifulSoup
from bing_image_downloader import downloader

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


#@client.event
#async def on_message(message):
#  if (message.author != client.user & message.content.startswith('$hello')):
#      await message.channel.send('Hello!')
#    if message.author == client.user:
#        return

#    if message.content.startswith('$hello'):
#        await message.channel.send('Hello!')
#response = google_images_download.googleimagesdownload()
#arguments = {"keywords": "rat", "limit": 1, "print_urls": True}
#paths = response.download(arguments)
bot = commands.Bot(command_prefix='!')
x = 0
@client.event
async def on_message(message):
    #    if (message == '@Rat Bot hello):
    if (message.author != client.user):
        #await message.channel.send(paths[0])
        #url="https://www.google.co.in/search?q=+rat+&source=lnms&tbm=isch"
        #header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
#}      
        #soup = get_soup(url,header)
        imageSearch = "rat animal cute"
        if (x != 0):
          downloader.download(imageSearch, limit=100, output_dir='downloads', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
          #x = 1
          
        
        filenames = os.listdir('downloads/' + imageSearch + '/')
        print(filenames)
        selected_file = "downloads/" + imageSearch + "/" + random.choice(filenames)
        print(selected_file)
        await message.channel.send(file=discord.File(selected_file))
#        await discord.send('Working!', file=discord.File(selected_file))
 #       await message.channel.send(    file=discord.File('_85925025_hognose03c.museumvictoria.jpg'))
        #      await message.channel.send('Hello!')
    elif message.author != client.user:
        await message.channel.send(message.content[::-1])


try:
    keep_alive()
    client.run(os.getenv("TOKEN"))
except discord.HTTPException as e:
    if e.status == 429:
        print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
        os.system("python restarter.py")
        os.system('kill 1')
        print(
            "The Discord servers denied the connection for making too many requests"
        )
        print(
            "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
        )
    else:
        raise e
