import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.db import Database
from psycopg2 import Error
from models.EmprestimoDisco import EmprestimoDisco

class EmprestimoDiscoController:
    def __init__(self):
        self.db = Database()

    def create(self, emprestimo_disco:EmprestimoDisco):
        params = (emprestimo_disco.get_codEmprestimo(), emprestimo_disco.get_codDisco())

        try:
            sql = "INSERT INTO emprestimo_disco (cod_emprestimo, cod_disco) VALUES (%s, %s);"
            self.db.execute_query(sql, params, False, True)

            return True
        except Error as e:
            print(f"Erro ao criar relação empréstimo-disco: {e}")
            return False

    def get_all(self):
        try:
            sql = "SELECT * FROM emprestimo_disco;"
            return self.db.execute_query(sql, (), True, False)
        
        except Error as e:
            print(f"Ocorreu um erro ao retornar relação empréstimo-disco: {e}")
            return []

    def get_by_emprestimo(self, cod_emprestimo: int):
        params = (cod_emprestimo,)

        try:
            sql = "SELECT * FROM emprestimo_disco WHERE cod_emprestimo = %s;"

            return self.db.execute_query(sql, params, True, False)

        except Error as e:
            print(f"Houve um erro ao retornar relação empréstimo-disco: {e}")
            return []


    def get_by_disco(self, cod_disco: int):
        params = (cod_disco,)

        try:
            sql = "SELECT * FROM emprestimo_disco WHERE cod_disco = %s;"

            return self.db.execute_query(sql, params, True, False)

        except Error as e:
            print(f"Houve um erro ao retornar relação empréstimo-disco: {e}")
            return []
    
    def get_emprestimo_disco_by_usuario(self, cpf_usuario:str):
        params = (cpf_usuario,)
        
        try:
            sql = "SELECT * FROM emprestimo_disco WHERE cod_emprestimo IN (SELECT emprestimos.codigo_emprestimo FROM emprestimos WHERE cpf_usuario = %s);"

            return self.db.execute_query(sql, params, True, False)

        except Error as e:
            print(f"Houve um erro ao retornar emprestimos: {e}")
            
            return []

    def get_by_genero_sessao(self, cod_emprestimo: int, cod_disco: int):
        params = (cod_emprestimo, cod_disco)

        try:
            sql = "SELECT * FROM emprestimo_disco WHERE cod_emprestimo = %s AND cod_disco = %s;"

            return self.db.execute_query(sql, params, True, False)

        except Error as e:
            print(f"Houve um erro ao retornar relação empréstimo-disco: {e}")
            return []

    def update_emprestimo(self, emprestimo_disco:EmprestimoDisco):
        params = (emprestimo_disco.get_codDisco(), emprestimo_disco.get_codEmprestimo())

        try:
            sql = "UPDATE emprestimo_disco SET cod_emprestimo = %s WHERE cod_disco = %s;"
            self.db.execute_query(sql, params, False, True)

            return True
        except Error as e:
            print(f"Ocorreu um erro ao alterar relação disco-emprestimo: {e}")
            return False

    def update_disco(self, emprestimo_disco:EmprestimoDisco):
        params = (emprestimo_disco.get_codDisco(), emprestimo_disco.get_codEmprestimo())

        try:
            sql = "UPDATE emprestimo_disco SET cod_disco = %s WHERE cod_emprestimo = %s;"
            self.db.execute_query(sql, params, False, True)

            return True
        except Error as e:
            print(f"Ocorreu um erro ao alterar relação disco-emprestimo: {e}")
            return False


    def delete(self, cod_emprestimo: int, cod_disco: int):
        params = (cod_emprestimo, cod_disco)

        try:
            sql = "DELETE FROM emprestimo_disco WHERE cod_emprestimo = %s AND cod_disco = %s;"
            self.db.execute_query(sql, params, False, True)
            return True
        except Error as e:
            print(f"Ocorreu um erro ao deletar relação disco-emprestimo: {e}")
            return False

    def delete_by_emprestimo(self, cod_emprestimo: int):
        params = (cod_emprestimo,)

        try:
            sql = "DELETE FROM emprestimo_disco WHERE cod_emprestimo = %s;"
            self.db.execute_query(sql, params, False, True)
            return True
        except Error as e:
            print(f"Ocorreu um erro ao deletar relação disco-emprestimo: {e}")
            return False

    def delete_by_disco(self, cod_disco: int):
        params = (cod_disco,)

        try:
            sql = "DELETE FROM emprestimo_disco WHERE cod_disco = %s;"
            self.db.execute_query(sql, params, False, True)
            return True
        except Error as e:
            print(f"Ocorreu um erro ao deletar relação disco-emprestimo: {e}")
            return False