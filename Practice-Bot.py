# This imports discord and allows python to accsess discord.
import discord
import discord.ext.commands
from discord.ext import commands

client = commands.Bot(command_prefix = '!')
TOKEN = PUT YOUR BOT TOKEN HERE


#   This command is very important, This command has starts the bot! and if you look at the bottom of atom or what ever console and you will see "This bot is online."
@client.event
async def on_ready():
    print('This bot is online.')
   


#  If you use the command !ping the bot will * it by 1000 and show your ms.
@client.command()
async def ping(ctx):
   await ctx.send(Pong! {f'Pong! {round(client.latency * 1000)}ms'}
   
#  A simple command and if you do !Hello the following command will be sent.
@client.command()
async def Hello(ctx):
    await ctx.send(Hello how are you doing? I know that I am doing bot-tastic!)
 
 
 #  There is no need to paste the token in here but just in case you want to to paste the toke just in The brackets copy and paste the token.   
client.run('TOKEN')

