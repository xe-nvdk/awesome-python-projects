# Hornero help you to manage yours InfluxDB servers.

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
bot = commands.Bot(command_prefix='!', description="Hornero is a worker, ready to help you to manage your InfluxDB OSS or InfluxDB Cloud instances.")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == bot.user:
        return

@bot.command(name='hello')
async def hello(ctx):
    response = str("Hi, I'm Hornero and I going to help you to manage your InfluxDB OSS and Cloud instances. Type '!help' to know about what I can do for you.")
    await ctx.send(response)

@bot.command(name='config', description='The config command allows you to list, create, delete and active configurations. Ex: !config create $name $influx_url $influx_token $influx_org.')
async def config(ctx, operation, *args):
    if operation == "ls":
        cmd = 'influx config ls'
        so = os.popen(cmd).read()
        await ctx.send(so)

    elif operation == "create":
        cmd = ('influx config create -n {} -u {} -t {} -o {}'.format(*args))
        so = os.popen(cmd).read()
        await ctx.send(so)

    elif operation == "active":
        cmd = ('influx config set -a -n {}'.format(*args))
        so = os.popen(cmd).read()
        await ctx.send(so)

    elif operation == "delete":
        cmd = 'influx config delete -n {}'.format(*args)
        so = os.popen(cmd).read()
        await ctx.send(so)
    else:
        await ctx.send("The parameter is not supported. I only suport 'ls', 'create' and 'delete'.")

@bot.command(name='bucket')
async def bucket(ctx, operation, *args):
    if operation == "ls":
        cmd = 'influx bucket ls'
        so = os.popen(cmd).read()
        await ctx.send(so)

    elif operation == "create":
        cmd = ('influx bucket create -n {} -r {}'.format(*args))
        so = os.popen(cmd).read()
        await ctx.send(so)

    elif operation == "delete":
        cmd = ('influx bucket delete -i {}'.format(*args))
        so = os.popen(cmd).read()
        await ctx.send(so)

    elif operation == "update":
        cmd = ('influx bucket update -i {} -n {} -r {}'.format(*args))
        so = os.popen(cmd).read()
        await ctx.send(so)

    else:
        await ctx.send("The parameter is not supported. I only suport 'ls', 'create', 'delete' and 'update'.")

@bot.command(name='user')
async def user(ctx, operation, *args):
    if operation == "ls":
        cmd = 'influx user ls'
        so = os.popen(cmd).read()
        await ctx.send(so)

    elif operation == "create":
        cmd = ('influx user create -n {} -p {}'.format(*args))
        so = os.popen(cmd).read()
        await ctx.send(so)

    elif operation == "delete":
        cmd = ('influx user delete -i {}'.format(*args))
        so = os.popen(cmd).read()
        await ctx.send(so)

    elif operation == "update":
        cmd = ('influx user update -i {} -n {}'.format(*args))
        so = os.popen(cmd).read()
        await ctx.send(so)

    else:
        await ctx.send("The parameter is not supported. I only suport 'ls', 'create', 'delete' and 'update'.")

@bot.command(name='dashboards')
async def user(ctx, *args):
        cmd = 'influx dashboards'
        so = os.popen(cmd).read()
        await ctx.send(so)


bot.run(TOKEN)
client.run(TOKEN)