# Discord Modules
import discord
from discord.ext import commands
from py_dotenv import dotenv
import discord_buttons_plugin
import os

# Other Modules
import sqlite3

# Inits
# Token Init
dotenv.read_dotenv('token/key.env')
token = os.environ.get('token')

# Client Init
client = commands.Bot(command_prefix='avdanos ')

# Database Inits
conn = sqlite3.connect('database/index.db')
db = conn.cursor()

# Events
@client.event
async def on_ready():
    print("Bot's ready!")

# Commands
@client.command()
async def download(ctx, type=None):
    embed = discord.Embed (
        title = 'Sorry, AvdanOS is still not ready yet.', 
        description = 'While making AvdanOS, you can contribute by joining our server: https://discord.gg/avdanos',
        color = 0xff1c1c
    )
    await ctx.send(embed=embed)

@client.command()
async def project(ctx):
    embed = discord.Embed(
    )

    embed.title = 'AvdanOS'
    embed.color = 0x4287f5
    embed.description = """AvdanOS is a concept operating system designed by Avdan, that we are trying to make it real. This is the main organization on GitHub for developing it. Here is the main repository that we use for developing the operating system."""

    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/801289484066488373/989793479087517846/Untitled.png')
    embed.add_field(name='Contributors', value='3')
    embed.add_field(name='Forks', value='4')
    embed.add_field(name='Stars', value='4.0')
    embed.add_field(name='Issues', value='3 Open')
    embed.add_field(name='License', value='GNU GPL V3')

    await ctx.send(embed=embed)

@client.command()
async def rank(ctx, user: discord.User = None):
    if user == None:
        user = ctx.author
    
    sql = 'SELECT EXISTS(SELECT 1 FROM ranks WHERE username=' + f'"{user.name}"' + ' LIMIT 1);'
    db.execute(sql)
    result = db.fetchall()[0][0]

    if result == 1:
        sql = 'SELECT rank from ranks WHERE username=' + f'"{user.name}"'
        db.execute(sql)
        result = db.fetchall()[0][0]
        
        embed = discord.Embed()

        embed.title = user.name
        embed.description = f'You are a {result}.'
        embed.add_field(name='Type', value=result)
        embed.color = 0x4287f5
        embed.set_thumbnail(url=user.avatar_url)

        await ctx.send(embed=embed)

    else:
        embed = discord.Embed()

        embed.title = 'User does not exist in database, yet.'
        embed.color = 0xff1c1c
        
        await ctx.send(embed=embed)



        
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.UserNotFound):
        embed = discord.Embed()

        embed.title = 'A parameter in a command did not match type.'
        embed.color = 0xff1c1c

        await ctx.send(embed=embed)
    else:
        print(error)

client.run(token)