import aioconsole
import colorama
import configparser
import discord
import json
import main
import utils

# basic initialization
colorama.init()
client = discord.Client()

# read config
try:
    with open("config.json") as f:
        config = json.load(f)
except FileNotFoundError:
    print("Please fill out a config.json file. \
           An example is provided for your convenience. Most settings can be left as-is. \
           If you are too confused at this point to fill out the form, this program is not right for you. \
           Good day.")
    exit(1)
client.config = config
token = config["token"]

@client.event
async def on_ready():
    client.loop.create_task(main.loop(client))

@client.event
async def on_message(message):
    print(utils.format_message(client, message))

# start bot
client.run(token, bot=False)
