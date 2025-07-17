import datetime

class Genero:
    def __init__(self, codigo:str, descricao:str):
        self.__codigo = codigo
        self.__descricao = descricao
        

    def get_codigo(self):
        return self.__codigo

    def get_descricao(self):
        return self.__descricao

    def set_codigo(self, codigo: str):
        self.__codigo = codigo

    def set_descricao(self, descricao: str):
        self.__descricao = descricao
