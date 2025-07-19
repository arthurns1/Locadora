import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.db import Database 
from psycopg2 import Error
from models.Genero import Genero

class GenerosController:
    def __init__(self):
        self.db = Database()

    def create(self, genero: Genero):
        params = (genero.get_descricao(),)

        try:
            sql = "INSERT INTO generos (codigo_genero, descricao) VALUES (DEFAULT, %s)"
            self.db.execute_query(sql, params, False, True)

            return True
        except Error as e:
            print(f"Erro ao adicionar genero: {e}")
            return False 

    def get_all(self):
        try:
            sql = "SELECT * FROM generos;"
            return self.db.execute_query(sql, (), True, False)
        
        except Error as e:
            print(f"Ocorreu um erro ao retornar generos:{e}")
            return []

    def get_by_codigo(self, codigo_genero:str):
        params = (codigo_genero,)

        try:
            sql = "SELECT * FROM generos WHERE codigo_genero = %s;"

            return self.db.execute_query(sql, params, True, False)

        except Error as e:
            print(f"Houve um erro ao retornar genero: {e}")
            
            return []

    def update(self, genero: Genero):
        params = (genero.get_descricao(), genero.get_codigo())

        try:
            sql = "UPDATE generos SET descricao= %s WHERE codigo_genero = %s;"
            self.db.execute_query(sql, params, False, True)

            return True
        except Error as e:
            print(f"Ocorreu um erro:{e}")
            
            return False

    def delete(self, codigo_genero:str):
        params = (codigo_genero,)

        try:
            sql = "DELETE FROM generos WHERE codigo_genero = %s;"
            self.db.execute_query(sql, params, False, True)

            return True
        except Error as e:
            print(f"Houve um erro ao tentar remover gênero: {e}")
            return False
