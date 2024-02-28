from discord import Interaction
from modelos.ComandoModelo import ComandoModelo

from modelos.interfaces.ManipuladorInterface import ManipuladorInterface

class JogarSubComando(ComandoModelo, ManipuladorInterface):
    def __init__(self, bot, grupo) -> None:
        super().__init__(
            bot=bot,
            nome="jogar",
            descricao="Inicie um jogo do BBB.",
            grupo=grupo,
            callback=self.manipular
        )

    async def manipular(self, interaction: Interaction):
        if f"{interaction.guild.id}" in self.bot.jogosBBB:
            self.bot.jogosBBB[f"{interaction.guild.id}"]["iniciado_por"] = interaction.user

            jogoBBB = self.bot.jogosBBB[f"{interaction.guild.id}"]
            iniciadoPor = jogoBBB["iniciado_por"]
            participantes = jogoBBB["participantes"]

            if len(participantes) > 2:
                await interaction.response.send_message(f"Participantes:\n```{[m.name for m in participantes]}```\nIniciado por {iniciadoPor.name}.")
            else:
                await interaction.response.send_message(f"É necessário no máximo 3 ou mais participantes...")
        else:
            await interaction.response.send_message(f"É necessário no máximo 3 ou mais participantes...")
        