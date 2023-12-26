from nextcord.ext import commands
from spreadsheetApi.spreadsheet import SheetApi


class Techniczne(commands.Cog, name="Techniczne"):
    """ """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def getRoles(self, ctx: commands.Context):

        for r in ctx.guild.roles:
            if str(r) == "@everyone":
                continue
            print(f"{r}  |  {r.id}")
        arkusz = SheetApi()
        print(arkusz.read('RoleID!A2:B4'))

    @commands.command()
    async def getUsers(self, ctx: commands.Context):
        for m in ctx.guild.members:
            print(f"{m.name}  |  {m.display_name}  |  {m.id}")

        arkusz = SheetApi()
        print(arkusz.read('Ludzie!A2:B5'))


def setup(bot: commands.Bot):
    bot.add_cog(Techniczne(bot))
