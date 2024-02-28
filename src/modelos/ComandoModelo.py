from discord.app_commands.commands import Command
from modelos.interfaces.ManipuladorInterface import ManipuladorInterface

class ComandoModelo(Command, ManipuladorInterface):
    def __init__(self, bot, nome, descricao, grupo, callback) -> None:
        super().__init__(
            name=nome, 
            description=descricao,
            parent=grupo,
            callback=callback
        )
        self.bot = bot