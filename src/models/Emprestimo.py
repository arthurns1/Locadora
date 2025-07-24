import datetime

class Emprestimo:
    def __init__(self, cpfCliente:str, codEmprestimo:str, prazo:datetime.datetime, dataEmprestimo:datetime.datetime, ativo:bool = True):
        self.__cpfCliente = cpfCliente
        self.__codEmprestimo = codEmprestimo
        self.__prazo = prazo
        self.__dataEmprestimo = dataEmprestimo
        self.__ativo = ativo

    def get_cpfCliente(self):
        return self.__cpfCliente

    def get_codEmprestimo(self):
        return self.__codEmprestimo

    def get_prazo(self):
        return self.__prazo

    def get_dataEmprestimo(self):
        return self.__dataEmprestimo

    def get_ativo(self):
        return self.__ativo

    def set_ativo(self, ativo: bool):
        self.__ativo = ativo

    def set_cpfCliente(self, cpfCliente:str):
        self.__cpfCliente = cpfCliente

    def set_codEmprestimo(self, codEmprestimo:str):
        self.__codEmprestimo = codEmprestimo

    def set_prazo(self, prazo:datetime.datetime):
        self.__prazo = prazo

    def set_dataEmprestimo(self, dataEmprestimo:datetime.datetime):
        self.__dataEmprestimo = dataEmprestimo