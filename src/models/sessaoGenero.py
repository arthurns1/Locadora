class SessaoGenero:
    def __init__(self, codGenero: int, numSessao: int):
        self.__codGenero = codGenero
        self.__numSessao = numSessao

    def get_codGenero(self):
        return self.__codGenero

    def get_numSessao(self):
        return self.__numSessao

    def set_codGenero(self, codGenero: int):
        self.__codGenero = codGenero

    def set_numSessao(self, numSessao: int):
        self.__numSessao = numSessao
    