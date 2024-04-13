import os
import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@bot.command()
async def mem(ctx):
    images = os.listdir('images')
    img_name = random.choice(images)

    with open(f'images/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def plastic(ctx):
    name = ['plastic1.jpg', 'plastic2.jpg', 'plastic3.jpg', 'plastic4.jpg', 'plastic5.jpg', 'plastic6.jpg', 'plastic7.jpg', 'plastic8.jpg', 'plastic9.jpg']
    img_name = random.choice(name)
    with open(f'images_eco/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send('Не выбрасывайте пластиковые бутылки! Лучше сделайте такую красивую и полезную вещь!😊')


bot.run("TOKEN")
