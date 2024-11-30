import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def joined(ctx, member: discord.Member):
     """da la bienvenida al usuario que se una al servidor"""
     await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
     
@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """repite una palabra la cantidad de veces que el usuario le pida. por ejemplo ($repeat numero de veces y la palabra)"""
    print(times, content)
    for i in range(times):
        await ctx.send(content)


    
bot.run("TOKEN SECRETO")    
