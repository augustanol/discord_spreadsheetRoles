from nextcord.ext import commands


class EasterEggi(commands.Cog, name="Easter Eggi"):
    """ """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def silencium(self, ctx: commands.Context):
        await ctx.send("Triplex")


def setup(bot: commands.Bot):
    bot.add_cog(EasterEggi(bot))
