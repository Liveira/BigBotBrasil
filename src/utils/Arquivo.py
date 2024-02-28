from json import loads

class Arquivo():

    @staticmethod
    def ler(caminho):
        return loads(open(caminho,'r').read())