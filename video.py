import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from discord import Game
 
Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()
 
@client.event
async def on_ready():
    await client.change_presence(game=Game(name='trekvogels'))
    print('trekvogel is ready :)')
   
@client.event
async def on_member_join(member):
    await client.send_message(member, "Welkom bij **__Google Nederland__**! Heb een leuke tijd en vergeet zeker niet om een command zoals **!janee** te proberen of natuurlijk **help**! Nog een fijn verblijf in **Google Nederland!**")
    await client.send_message(member, "-------------------------------------------------------------------")
    await client.send_message(member, "Lees de regels zodat je geen waarschuwingen krijgt!")
    await client.send_message(member, "Hou je het wel gezellig?!")
    await client.send_message(member, "-------------------------------------------------------------------")
   
   
@client.event
async def on_message(message):
    if message.content.startswith('!janee'):
        randomlist = ['Ja','Nee']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!vriend'):
        randomlist = ['20%','30%','40%','50%','60%','70%','80%','90%','100%']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == '!test':
        await client.send_message(message.channel,'test xD
     
client.run('NTYyNjc4Mzk3MTUxNjA4ODM0.XKzqQg.pqaWPUQUTsDvekSA2YXNooVEX48')
