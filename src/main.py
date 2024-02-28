from cliente.Cliente import Cliente
from utils.Arquivo import Arquivo

conteudo = Arquivo.ler("config.json")

cliente = Cliente()
cliente.run(conteudo["TOKEN"])