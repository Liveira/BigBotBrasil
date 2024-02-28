from discord.app_commands import Group

class GrupoModelo(Group):
    def __init__(self, bot, nome, descricao):
        super().__init__(
            name=nome,
            description=descricao
        )

        self.bot = bot