import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.db import Database 
from models.Emprestimo import Emprestimo
from psycopg2 import Error

class EmprestimosController:
    def __init__(self):
        self.db = Database()

    def create(self, emprestimo: Emprestimo):
        params = ( emprestimo.get_prazo(), emprestimo.get_dataEmprestimo(), emprestimo.get_cpfCliente())

        try:
            sql = "INSERT INTO emprestimos (codigo_emprestimo, prazo, data_emprestimo, cpf_cliente) VALUES (DEFAULT, %s, %s, %s);"
            self.db.execute_query(sql, params, False, True)

            return True
        except Error as e:
            print(f"Erro ao adicionar emprestimo: {e}")
            return False 

    def get_all(self):
        try:
            sql = "SELECT * FROM emprestimos;"
            return self.db.execute_query(sql, (), True, False)
        
        except Error as e:
            print(f"Ocorreu um erro ao retornar discos: {e}")
            return []

    def get_by_codigo(self, codigo_emprestimo: int):
        params = (codigo_emprestimo,)

        try:
            sql = "SELECT * FROM emprestimos WHERE codigo_emprestimo = %s;"

            return self.db.execute_query(sql, params, True, False)

        except Error as e:
            print(f"Houve um erro ao retornar emprestimos: {e}")
            
            return []

    def update(self, emprestimo: Emprestimo):
        params = (emprestimo.get_prazo(), emprestimo.get_dataEmprestimo(), emprestimo.get_cpfCliente(), emprestimo.get_codigo())

        try:
            sql = "UPDATE emprestimos SET prazo = %s, data_emprestimo = %s, cpf_cliente = %s WHERE codigo_emprestimo = %s;"
            self.db.execute_query(sql, params, False, True)

            return True
        except Error as e:
            print(f"Ocorreu um erro ao alterar disco:{e}")
            
            return False

    def delete(self, codigo_emprestimo:int):
        params = (codigo_emprestimo,)

        try:
            sql = "DELETE FROM emprestimos WHERE codigo_emprestimo = %s;"
            self.db.execute_query(sql, params, False, True)

            return True
        except Error as e:
            print(f"Houve um erro ao remover emprestimo:  {e}")
            return False