from nextcord.ext import commands


class Role(commands.Cog, name="Role"):
    """ """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def getRoles(self, ctx: commands.Context):

        for r in ctx.guild.roles:
            if str(r) == "@everyone":
                continue
            print(f"{r}  |  {r.id}")

    @commands.command()
    async def getUsers(self, ctx: commands.Context):
        for m in ctx.guild.members:
            print(f"{m.name}  |  {m.display_name}  |  {m.id}")


def setup(bot: commands.Bot):
    bot.add_cog(Role(bot))
