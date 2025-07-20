import datetime

class Genero:
    def __init__(self, codigo:str,nome:str , descricao:str):
        self.__codigo = codigo
        self.__nome = nome
        self.__descricao = descricao
        

    def get_codigo(self):
        return self.__codigo

    def get_nome(self):
        return self.__nome
    
    def get_descricao(self):
        return self.__descricao

    def set_codigo(self, codigo: str):
        self.__codigo = codigo

    def set_nome(self, nome: str):
        self.__nome = nome

    def set_descricao(self, descricao: str):
        self.__descricao = descricao
