from nextcord.ext import commands
from nextcord import Embed
from spreadsheetApi.spreadsheet import SheetApi


class Role(commands.Cog, name="Role"):
    """ """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def printDcRoles(self, ctx: commands.Context):
        embed = Embed(colour=0xe67e22, title='Role pobrane z Discorda')

        for member in ctx.guild.members:

            roles = ''

            for role in member.roles:
                if str(role) == '@everyone':
                    continue
                roles += f'{role}\n'

            embed.add_field(name=str(member.display_name), value=roles)
            embed.add_field(name='\u200b', value='\u200b')
            embed.add_field(name='\u200b', value='\u200b')

        await ctx.send(embed=embed)

    @commands.command()
    async def printSheetRoles(self, ctx: commands.Context):

        users_sheet = SheetApi().read('Ludzie!A1:E5')
        # role_sheet = SheetApi().read('RoleID!A1:B4')
        existing_roles = users_sheet[0][2:len(users_sheet[0])]

        print(users_sheet)

        embed = Embed(colour=0xe67e22, title='Role pobrane z arkusza')

        for member in users_sheet[1:len(users_sheet)]:

            roles = ''

            for i in range(2, len(member)):
                role = member[i]
                if role == 'TRUE':
                    roles += f'{existing_roles[i-2]}\n'

            embed.add_field(name=str(member[0]), value=roles)
            embed.add_field(name='\u200b', value='\u200b')
            embed.add_field(name='\u200b', value='\u200b')

        await ctx.send(embed=embed)

    @commands.command()
    async def updateRoles(self, ctx: commands.Context):

        users_sheet = SheetApi().read('Ludzie!A1:E5')
        role_sheet = SheetApi().read('RoleID!A1:B4')
        DiscordRoles = {}
        SheetRoles = {}
        Roles_to_delete = {}
        Roles_to_add = {}

        # pobieranie ról z dc do słownika: klucz id użtkownika, wartości: lista z id ról
        for member in ctx.guild.members:
            if str(member.id) not in ("1184476353903460474", "1141665704786001950"):
                roles = []
                for role in member.roles:
                    if str(role) not in ("@everyone", "admin"):
                        roles.append(int(role.id))

                DiscordRoles[int(member.id)] = roles

        # pobieranie ról z arkusza do słownika
        Roles_id = {}

        for role in role_sheet[1:len(role_sheet)]:
            Roles_id[role[0]] = role[1]

        for member in users_sheet[1:len(users_sheet)]:
            roles = []
            for i in range(2, len(member)):
                role = member[i]
                if role == 'TRUE':
                    roles.append(int(Roles_id[users_sheet[0][i]]))
            SheetRoles[int(member[1])] = roles

        # porównanie
        for member in DiscordRoles:
            roles = []
            for role in DiscordRoles[member]:
                if role not in SheetRoles[member]:
                    roles.append(role)
                Roles_to_delete[member] = roles

        for member in SheetRoles:
            roles = []
            for role in SheetRoles[member]:
                if role not in DiscordRoles[member]:
                    roles.append(role)
                Roles_to_add[member] = roles

        # dodawanie i usuwanie ról

        embed = Embed(colour=0xe67e22, title='Aktualizacja ról')

        for member in DiscordRoles:
            text = ""
            if member in Roles_to_add:

                text += "\nDodano role: "

                for role in Roles_to_add[member]:
                    m = ctx.guild.get_member(member)
                    r = ctx.guild.get_role(role)
                    await m.add_roles(r)

                    text += f'\n{r.name}'

            if member in Roles_to_delete:

                text += "\nUsunięto role: "

                for role in Roles_to_delete[member]:
                    m = ctx.guild.get_member(member)
                    r = ctx.guild.get_role(role)
                    await m.remove_roles(r)

                    text += f'\n{r.name}'

            if member not in Roles_to_add and member not in Roles_to_delete:
                text = 'Brak zmian'

            embed.add_field(name=str(ctx.guild.get_member(
                member).display_name), value=text)
            embed.add_field(name='\u200b', value='\u200b')
            embed.add_field(name='\u200b', value='\u200b')

        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Role(bot))
