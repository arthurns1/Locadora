class Usuario:
    def __init__(self, nome:str, login:str, idade:int, senha:str, cpf:str, cargo:str):
        self.__nome = nome
        self.__login = login
        self.__idade = idade
        self.__senha = senha
        self.__cpf = cpf
        self.__cargo = cargo

    def get_nome(self):
        return self.__nome

    def get_login(self):
        return self.__login

    def get_idade(self):
        return self.__idade

    def get_senha(self):
        return self.__senha

    def get_cpf(self):
        return self.__cpf

    def get_cargo(self,):
        return self.__cargo

    def set_nome(self, nome:str):
        self.__nome = nome

    def set_login(self, login:str):
        self.__login = login

    def set_idade(self, idade:int):
        self.__idade = idade

    def set_senha(self, senha:str):
        self.__senha = senha

    def set_cpf(self, cpf:str):
        self.__cpf = cpf

    def set_cargo(self, cargo:str):
        self.__cargo = cargo