from discord.ext import commands


class Spreadsheet(commands.Cog, name="Spreadsheet"):
    """Receives ping commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def spreadsheet(self, ctx: commands.Context):
        """/Sprawdza czy bot działa"""
        await ctx.send("Triplex")


async def setup(bot: commands.Bot):
    await bot.add_cog(Spreadsheet(bot))
