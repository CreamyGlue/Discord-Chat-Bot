import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')## the exclemation mark is for intiating the bots commands

##on ready will tell you when the bot is ready
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Despacito!'))##the status and game can be changes by editing
    print ('bot is ready')
##will show the member join in the console 
@client.event
async def on_member_join(member):
    print(f'{member} has joined a server')
##When a user leaves the server it will show up on the console.
@client.event
async def on_member_remove(member):
    print(f'{member} has left the server <3')
##!ping is a command you can use in the discord and this will tell you the ping of the bot in the server
@client.command()
async def ping(ctx):
    await ctx.send(f'ping! {round(client.latency * 1000)}ms')

##!clear is a command that clears the last 5 or whatever you specify in amount to clear by default I set it to five comments
@client.command()
async def clear(ctx, amount=5):
    amount=amount+1
    await ctx.channel.purge(limit=amount)
##!kick then do the @ of the user  Ex: !kick @name
@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
##!ban then do the @ of the user Ex: !ban @name
@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)  


    
client.run('')## this will be filled in with the ID to link your bot with the program.