import discord
from discord.ext import commands
from bot_logic import gen_pass, flip_coin

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = '$', intents=intents)

#print de login----------------------
@bot.event
async def on_ready():
    print(f'logado como {bot.user}')
#------------------------------------

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello! i am botzinho')

@bot.command()
async def bye(ctx):
    await ctx.send(f'\U0001f642')

@bot.command()
async def createpass(ctx, length = 10):
    await ctx.send(gen_pass(length))
    
@bot.command()
async def flipcoin(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def joined(ctx, *, member: discord.Member):
    await ctx.send(f'{member} joined on {member.joined_at}')

@bot.command()
async def repeat(ctx, times: int = 2, content = 'repeating'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
