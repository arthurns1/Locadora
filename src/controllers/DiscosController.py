import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.db import Database 
from models.Disco import Disco
from psycopg2 import Error

class DiscosController:
    def __init__(self):
        self.db = Database()

    def create(self, disco: Disco):
        params = (disco.get_numSessao(), disco.get_codigoGenero(), disco.get_titulo(), disco.get_lancamento(), disco.get_diretor(), disco.get_classInd(), disco.is_emprestado())

        try:
            sql = "INSERT INTO discos (codigo_disco, num_sessao, cod_genero, titulo, lancamento, diretor, class_ind, emprestado) VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s);"
            self.db.execute_query(sql, params, False, True)

            return True
        except Error as e:
            print(f"Erro ao adicionar disco: {e}")
            return False 

    def get_all(self):
        try:
            sql = "SELECT * FROM discos;"
            return self.db.execute_query(sql, (), True, False)
        
        except Error as e:
            print(f"Ocorreu um erro ao retornar discos: {e}")
            return []

    def get_by_codigo(self, codigo_disco: int):
        params = (codigo_disco,)

        try:
            sql = "SELECT * FROM discos WHERE codigo_disco = %s;"

            return self.db.execute_query(sql, params, True, False)

        except Error as e:
            print(f"Houve um erro ao retornar discos: {e}")
            
            return []

    def set_emprestado(self, codigo_disco: int, emprestado: bool):
        params = (emprestado, codigo_disco)

        try:
            sql = "UPDATE discos SET emprestado = %s WHERE codigo_disco = %s;"
            self.db.execute_query(sql, params, False, True)

            return True
        except Error as e:
            print(f"Ocorreu um erro ao atualizar status de empréstimo do disco: {e}")
            return False

    def update(self, disco: Disco):
        params = (disco.get_numSessao(), disco.get_codigoGenero(), disco.get_titulo(), disco.get_lancamento(), disco.get_diretor(), disco.get_classInd(), disco.get_codigo())

        try:
            sql = "UPDATE discos SET num_sessao = %s, cod_genero = %s, titulo = %s, lancamento = %s, diretor = %s, class_ind = %s  WHERE codigo_disco = %s;"
            self.db.execute_query(sql, params, False, True)

            return True
        except Error as e:
            print(f"Ocorreu um erro ao alterar disco:{e}")
            
            return False

    def delete(self, codigo_disco:int):
        params = (codigo_disco,)

        try:
            sql = "DELETE FROM discos WHERE codigo_disco = %s;"
            self.db.execute_query(sql, params, False, True)

            return True
        except Error as e:
            print(f"Houve um erro ao remover disco:  {e}")
            return False