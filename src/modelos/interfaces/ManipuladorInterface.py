from discord import Interaction
import abc

class ManipuladorInterface(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    async def manipular(self, interaction: Interaction):
        pass