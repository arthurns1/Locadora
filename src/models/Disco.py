import datetime

class Disco:
    def __init__(self, codigo:int, numSessao:int, codigoGenero: int, titulo:str, lancamento:datetime, diretor:str, classInd: int):
        self.__codigo = codigo
        self.__numSessao = numSessao
        self.__codigoGenero = codigoGenero
        self.__titulo = titulo
        self.__lancamento = lancamento
        self.__diretor = diretor
        self.__classInd = classInd

    def get_codigo(self):
        return self.__codigo

    def get_titulo(self):
        return self.__titulo

    def get_lancamento(self):
        return self.__lancamento

    def get_diretor(self):
        return self.__diretor

    def get_classInd(self):
        return self.__classInd

    def get_codigoGenero(self):
        return self.__codigoGenero

    def get_numSessao(self):
        return self.__numSessao

    def set_codigo(self, codigo: str):
        self.__codigo = codigo

    def set_codigoGenero(self, codigoGenero: str):
        self.__codigoGenero = codigoGenero

    def set_titulo(self, titulo:str):
        self.__titulo = titulo

    def set_lancamento(self, lancamento:datetime):
        self.__lancamento = lancamento

    def set_diretor(self, diretor: str):
        self.__diretor = diretor

    def set_classInd(self, classInd: int):
        self.__classInd = classInd