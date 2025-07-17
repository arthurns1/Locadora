import datetime

class Emprestimo:
    def __init__(self, cpfCliente:str, codEmprestimo:str, prazo:int, dataEmprestimo:datetime):
        self.__cpfCliente = cpfCliente
        self.__codEmprestimo = codEmprestimo
        self.__prazo = prazo
        self.__dataEmprestimo = dataEmprestimo

    def get_cpfCliente(self):
        return self.__cpfCliente

    def get_codEmprestimo(self):
        return self.__codEmprestimo

    def get_prazo(self):
        return self.__prazo

    def get_dataEmprestimo(self):
        return self.__dataEmprestimo
    
    def set_cpfCliente(self, cpfCliente:str):
        self.__cpfCliente = cpfCliente

    def set_codEmprestimo(self, codEmprestimo:str):
        self.__codEmprestimo = codEmprestimo

    def set_prazo(self, prazo:datetime.datetime):
        self.__prazo = prazo

    def set_dataEmprestimo(self, dataEmprestimo:datetime.datetime):
        self.__dataEmprestimo = dataEmprestimo