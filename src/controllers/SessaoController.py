import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.db import Database
from psycopg2 import Error
from models.Sessao import Sessao
 
class SessaoController:
    def __init__(self):
        self.db = Database()

    def create(self, sessao:Sessao):
        params = (sessao.get_corredor(), sessao.get_numero())

        try:
            sql = "INSERT INTO sessoes (numero, corredor) VALUES (DEFAULT, %s);"
            self.db.execute_query(sql, params, False, True)

            return True
        except Error as e:
            print(f"Erro ao adicionar sessão: {e}")
            return False

    def get_all(self):
        try:
            sql = "SELECT * FROM sessoes;"
            return self.db.execute_query(sql, (), True, False)
        
        except Error as e:
            print(f"Ocorreu um erro ao retornar sessões: {e}")
            return []

    def get_by_numero(self, numero: int):
        params = (numero,)

        try:
            sql = "SELECT * FROM sessoes WHERE numero = %s;"

            return self.db.execute_query(sql, params, True, False)

        except Error as e:
            print(f"Houve um erro ao retornar sessão: {e}")
            return []

    def update(self, sessao:Sessao):
        params = (sessao.get_corredor(), sessao.get_numero())

        try:
            sql = "UPDATE sessoes SET corredor = %s WHERE numero = %s;"
            self.db.execute_query(sql, params, False, True)

            return True
        except Error as e:
            print(f"Ocorreu um erro ao alterar sessão: {e}")
            return False

    def delete(self, numero: int):
        params = (numero,)

        try:
            sql = "DELETE FROM sessoes WHERE numero = %s;"
            self.db.execute_query(sql, params, False, True)
            return True
        except Error as e:
            print(f"Ocorreu um erro ao deletar sessão: {e}")
            return False