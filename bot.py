import os
from dotenv import load_dotenv
import discord
from discord.ext import commands


def bot_setup():
    intents = discord.Intents.all()

    client = commands.Bot(command_prefix="?", intents=intents)

    load_dotenv()

    @client.event
    async def on_ready():
        print(f"\n{client.user.name} has been connected to Discord\n")

        for folder in os.listdir("modules"):
            if os.path.exists(os.path.join("modules", folder, "cog.py")):
                await client.load_extension(f"modules.{folder}.cog")
                print(f"\nBot z {folder} dodany\n")

    client.run(os.getenv("DISCORD_TOKEN"))


def main():

    bot_setup()


if __name__ == '__main__':
    main()
