class EmprestimoDisco:
    def __init__(self, codDisco:int, codEmprestimo:int, quantidade:int):
        self.__codDisco = codDisco
        self.__codEmprestimo = codEmprestimo
        self.__quantidade = quantidade

    def get_codDisco(self):
        return self.__codDisco

    def codEmprestimo(self):
        return self.__codEmprestimo

    def get_quantidade(self):
        return self.__quantidade

    def set_codDisco(self, codDisco: int):
        self.__codDisco = codDisco

    def set_codEmprestimo(self, codEmprestimo:int):
        self.__codEmprestimo = codEmprestimo

    def set_quantidade(self, quantidade:int):
        self.__quantidade = quantidade

    