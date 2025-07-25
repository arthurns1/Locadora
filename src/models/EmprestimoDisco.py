class EmprestimoDisco:
    def __init__(self, codDisco:int, codEmprestimo:int):
        self.__codDisco = codDisco
        self.__codEmprestimo = codEmprestimo

    def get_codDisco(self):
        return self.__codDisco

    def get_codEmprestimo(self):
        return self.__codEmprestimo

    def set_codDisco(self, codDisco: int):
        self.__codDisco = codDisco

    def set_codEmprestimo(self, codEmprestimo:int):
        self.__codEmprestimo = codEmprestimo

    