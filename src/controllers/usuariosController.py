import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.db import Database 
from models.Usuario import Usuario
from psycopg2 import Error

class UsuariosController:
    def __init__(self):
        self.db = Database()

    def create(self, usuario: Usuario):
        params = (usuario.get_nome(), usuario.get_login(), usuario.get_idade(), usuario.get_senha(), usuario.get_cpf(), usuario.get_cargo())

        try:
            sql = "INSERT INTO usuarios (nome, login, idade, senha, cpf, cargo) VALUES (%s, %s, %s, %s, %s, %s)"
            self.db.execute_query(sql, params, False, True)

            return True
        except Error as e:
            print(f"Erro ao adicionar usuário: {e}")
            return False 

    def get_all(self):
        try:
            sql = "SELECT * FROM usuarios;"
            return self.db.execute_query(sql, (), True, False)
        
        except:
            return []

    def get_by_cpf(self, cpf:str):
        params = (cpf,)

        try:
            sql = "SELECT * FROM usuarios WHERE cpf = %s;"

            return self.db.execute_query(sql, params, True, False)

        except Error as e:
            print(e)
            
            return []

    def get_by_login(self, login:str):
        params = (login,)

        try:
            sql = "SELECT * FROM usuarios WHERE login = %s;"

            return self.db.execute_query(sql, params, True, False)

        except Error as e:
            print(e)
            
            return []

    def update(self, usuario: Usuario):
        params = (usuario.get_nome(), usuario.get_login(), usuario.get_idade(), usuario.get_senha(), usuario.get_cargo(), usuario.get_cpf())

        try:
            sql = "UPDATE usuarios SET nome= %s, login= %s, idade= %s, senha= %s, cargo = %s WHERE cpf = %s;"
            self.db.execute_query(sql, params, False, True)

            return True
        except Error as e:
            print(f"Ocorreu um erro:{e}")
            
            return False

    def delete(self, cpf:str):
        params = (cpf,)

        try:
            sql = "DELETE FROM usuarios WHERE cpf = %s;"
            self.db.execute_query(sql, params, False, True)

            return True
        except:
            return False

