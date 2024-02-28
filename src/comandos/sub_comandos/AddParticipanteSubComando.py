from discord import Interaction, Member
from modelos.ComandoModelo import ComandoModelo
from modelos.interfaces.ManipuladorInterface import ManipuladorInterface

class AddParticipanteSubComando(ComandoModelo, ManipuladorInterface):
    def __init__(self, bot, grupo) -> None:
        super().__init__(
            bot=bot,
            nome="addparticipante",
            descricao="Adicione um participante ao jogo.",
            grupo=grupo,
            callback=self.manipular
        )
    
    async def manipular(self, interaction: Interaction, membro: Member):
        if f"{interaction.guild.id}" not in self.bot.jogosBBB:
            self.bot.jogosBBB[f"{interaction.guild.id}"] = dict({
                "iniciado_por": None,
                "participantes": list()
            })

        self.bot.jogosBBB[f"{interaction.guild.id}"]["participantes"].append(membro)
        
        await interaction.response.send_message(f"O participante \`{membro.name}\` foi adicionado ao jogo!")