import discord
import json
import storage
import schedule
import asyncio


def run_Gordon():
    with open("config.json", "r") as token_file:
        token = json.load(token_file)["token"]

    intents = discord.Intents.default()
    intents.typing = False
    intents.presences = False
    intents.messages = True
    intents.message_content = True
    intents.reactions = True

    TOKEN = token
    client = discord.Client(intents=intents)

    async def send_grocery_list():
        storage.export_list()

    @client.event
    async def on_ready():
        print("Gordon is online!")

        # not working yet
        schedule.every().wednesday.at("12:00").do(asyncio.run, send_grocery_list)

    @client.event
    async def on_reaction_add(reaction, user):
        if user == client.user:
            return

        react_emoji = "\U0001F34D"

        storage.store_message(reaction.message.content)
        await reaction.message.add_reaction(react_emoji)

    client.run(TOKEN)
