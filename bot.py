import discord
import json
import storage


def run_Gordon():
    with open("config.json", "r") as token_file:
        token = json.load(token_file)["token"]

    TOKEN = token
    client = discord.Client()

    @client.event
    async def on_ready():
        print("Gordon is online!")

    @client.event
    async def on_message(message):
        react_emoji = "\U0001F34D"

        if message.author == client.user:
            return

        storage.store_message(message)
        await message.add_reaction(react_emoji)

    client.run(TOKEN)
