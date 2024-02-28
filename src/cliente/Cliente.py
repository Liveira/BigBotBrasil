from discord import Intents
from discord.ext.commands import Bot
from comandos.BbbGrupo import BbbGrupo

class Cliente(Bot):

    def __init__(self) -> None:
        super().__init__(command_prefix="-", intents=Intents.all())

        self.jogosBBB = dict()

    async def on_ready(self):
        print(f'Entrou como {self.user}!')
        
        print("Carregando comandos...")
        await self.carregar_comandos()
        try:
            await self.tree.sync()
            print("Comandos carregados!")
        except Exception as e:
            print(e)

    async def carregar_comandos(self):
        self.tree.add_command(BbbGrupo(self))

        # for arquivo in listdir("src\comandos"):
        #     if not arquivo[:-3].__contains__("pycach"):
                # module = __import__(f"src\comandos\{arquivo}")
                # class_ = getattr(module, arquivo[:-3])
                # instance = class_()

                # _module = import_module("..\\comandos\\" + arquivo, package=__package__)
                # class_ = getattr(_module, arquivo[:-3])
                # instance = class_()
                # print(instance)

                # module = __import__(f"src\comandos\{arquivo}")
                # print(module)
                
                # await self.load_extension(f"comandos.{arquivo[:-3]}")