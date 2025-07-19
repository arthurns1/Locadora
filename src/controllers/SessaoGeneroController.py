import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.db import Database
from psycopg2 import Error
from models.SessaoGenero import SessaoGenero
 
class SessaoGeneroController:
    def __init__(self):
        self.db = Database()

    def create(self, sessaoGenero:SessaoGenero):
        params = (sessaoGenero.get_numSessao(), sessaoGenero.get_codGenero())

        try:
            sql = "INSERT INTO genero_sessao (num_sessao, cod_genero) VALUES (%s, %s);"
            self.db.execute_query(sql, params, False, True)

            return True
        except Error as e:
            print(f"Erro ao criar relação sessão-genero: {e}")
            return False

    def get_all(self):
        try:
            sql = "SELECT * FROM genero_sessao;"
            return self.db.execute_query(sql, (), True, False)
        
        except Error as e:
            print(f"Ocorreu um erro ao retornar relação sessão-genero: {e}")
            return []

    def get_by_sessao(self, numero: int):
        params = (numero,)

        try:
            sql = "SELECT * FROM genero_sessao WHERE num_sessao = %s;"

            return self.db.execute_query(sql, params, True, False)

        except Error as e:
            print(f"Houve um erro ao retornar relação sessão-genero: {e}")
            return []


    def get_by_genero(self, codigo_genero: int):
        params = (codigo_genero,)

        try:
            sql = "SELECT * FROM genero_sessao WHERE cod_genero = %s;"

            return self.db.execute_query(sql, params, True, False)

        except Error as e:
            print(f"Houve um erro ao retornar relação sessão-genero: {e}")
            return []


    def get_by_genero_sessao(self, codigo_genero: int, num_sessao: int):
        params = (codigo_genero, num_sessao)

        try:
            sql = "SELECT * FROM genero_sessao WHERE cod_genero = %s AND num_sessao = %s;"

            return self.db.execute_query(sql, params, True, False)

        except Error as e:
            print(f"Houve um erro ao retornar relação sessão-genero: {e}")
            return []

    def update_genero(self, sessao_genero:SessaoGenero):
        params = (sessao_genero.get_codGenero(), sessao_genero.get_numSessao())

        try:
            sql = "UPDATE genero_sessao SET cod_genero = %s WHERE num_sessao = %s;"
            self.db.execute_query(sql, params, False, True)

            return True
        except Error as e:
            print(f"Ocorreu um erro ao alterar relação sessão-genero: {e}")
            return False

    def update_sessao(self, sessao_genero:SessaoGenero):
        params = (sessao_genero.get_numSessao(), sessao_genero.get_codGenero())

        try:
            sql = "UPDATE genero_sessao SET num_sessao = %s WHERE cod_genero = %s;"
            self.db.execute_query(sql, params, False, True)

            return True
        except Error as e:
            print(f"Ocorreu um erro ao alterar relação sessão-genero: {e}")
            return False

    
    def delete(self, numero: int, codigo_genero: int):
        params = (numero, codigo_genero)

        try:
            sql = "DELETE FROM genero_sessao WHERE num_sessao = %s AND cod_genero = %s;"
            self.db.execute_query(sql, params, False, True)
            return True
        except Error as e:
            print(f"Ocorreu um erro ao deletar sessão: {e}")
            return False

    def delete_by_sessao(self, numero: int):
        params = (numero,)

        try:
            sql = "DELETE FROM genero_sessao WHERE num_sessao = %s;"
            self.db.execute_query(sql, params, False, True)
            return True
        except Error as e:
            print(f"Ocorreu um erro ao deletar sessão: {e}")
            return False

    def delete_by_genero(self, codigo_genero: int):
        params = (codigo_genero,)

        try:
            sql = "DELETE FROM genero_sessao WHERE cod_genero = %s;"
            self.db.execute_query(sql, params, False, True)
            return True
        except Error as e:
            print(f"Ocorreu um erro ao deletar sessão: {e}")
            return False