from comandos.sub_comandos.AddParticipanteSubComando import AddParticipanteSubComando
from comandos.sub_comandos.JogarSubComando import JogarSubComando
from modelos.GrupoModelo import GrupoModelo

class BbbGrupo(GrupoModelo):
    def __init__(self, bot):
        super().__init__(
            bot=bot,
            nome="bbb", 
            descricao="Exibe os comandos do BBB!",
        )
        self.add_command(JogarSubComando(bot=bot, grupo=self))
        self.add_command(AddParticipanteSubComando(bot=bot, grupo=self))

