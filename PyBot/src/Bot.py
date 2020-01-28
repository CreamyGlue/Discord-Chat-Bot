import discord
from discord.ext import commands
import random


client = commands.Bot(command_prefix ='!')  ## the exclemation mark is for intiating the bots commands
print("Welcome to py bot")
print("Lets start off with getting a token id for the bot. If you dont know what this is look at the docs for more info.")
token = input("Now, please enter token: ")


##on ready will tell you when the bot is ready
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game('Ready for commands'))  ##the status and game can be changed by editing this activity
    print('bot is ready')


##will show the member join in the console
@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')


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
    amount = amount + 1
    await ctx.channel.purge(limit=amount)
    print(f'{amount} messages have been cleared from the server')


##!kick then do the @ of the user  Ex: !kick @name
@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    print (f'{member} has been kicked from the server')


##!ban then do the @ of the user Ex: !ban @name
@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    print(f'{member} Has been banned from the server.')

@client.command()
async  def inspireMe(ctx):
    quotes = ['“Do one thing every day that scares you.” – Eleanor Roosevelt',
              '“To be the best, you must be able to handle the worst.” – Wilson Kanadi',
              '“There’s a four-letter word you must use when you get rejected… next.” – Jack Canfield',
              '“It is during our darkest moments that we must focus on the light.” – Aristotle Onassis',
              '“If you are interested, you’ll do what’s convenient. If you’re committed, you’ll do whatever it takes.” – John Assaraf',
              '“It’s never too late to start creating the life you desire.” – Dawn Clark',
              '“Everything you’ve ever wanted is on the other side of fear.” – George Addair',
              '“In the middle of every difficulty, lies opportunity.” – Albert Einstein',
              '“If you don’t like the road you’re walking, start paving another one.” – Dolly Parton',
              '“Strive not to be a success, but rather to be of value.” – Albert Einstein',
              '“The only way to do great work is to love what you do.” – Steve Jobs',
              '“It does not matter how slow you go, as long as you do not stop.” – Confucius',
              '“The only limits in our life are those we impose on ourselves.” – Bob Proctor',
              '“Start where you are, with what you have, and that will always lead you into something greater.” – Mary Morrissey']
    await ctx.send(f'{random.choice(quotes)}')

client.run(token)  ## this will be filled in with the ID to link your bot with the program.