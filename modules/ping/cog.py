from discord.ext import commands


class Ping(commands.Cog, name="Ping"):
    """Receives ping commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """/Sprawdza czy bot działa"""
        await ctx.send("Triplex")

    @commands.command()
    async def ping2(self, ctx: commands.Context):
        """/Sprawdza czy bot działa"""
        await ctx.send("Triplex")


async def setup(bot: commands.Bot):
    await bot.add_cog(Ping(bot))
