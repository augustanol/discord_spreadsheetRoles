import os
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands

def bot_setup():
    intents = nextcord.Intents.all()

    client = commands.Bot(command_prefix="?", intents=intents)

    load_dotenv()

    @client.event
    async def on_ready():
        print(f"\n{client.user.name} has been connected to Discord\n")

    for folder in os.listdir("modules"):
        if os.path.exists(os.path.join("modules", folder, "cog.py")):
            client.load_extension(f"modules.{folder}.cog")
            print(f"\nFunkcje z {folder} dodane")

    #client.run(os.getenv("DISCORD_TOKEN"))
    client.run(os.getenv("DISCORD_TOKEN"))


def main():

    bot_setup()


if __name__ == '__main__':
    main()
