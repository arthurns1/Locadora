import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '...')))
from src.models.Emprestimo import Emprestimo
from src.controllers.EmprestimosController import EmprestimosController

emprestimosController = EmprestimosController()

codigo_emprestimo = 1

def teste_create():
    emprestimo = Emprestimo(codigo_emprestimo, "Teste", "2023-01-01", "2023-01-10")

    print(usuariosController.create(usuario))

    print(usuariosController.get_by_cpf(cpf))

    usuariosController.delete(cpf)

def teste_update():
    usuario = Usuario("Teste", "teste", 20, "123456", cpf, "Usuario")

    print(usuariosController.create(usuario))

    print(usuariosController.get_by_cpf(cpf))
    
    usuario = Usuario("Teeste","Teeste", 15, "123", cpf, "Admin")
    
    print(usuariosController.update(usuario))

    print(usuariosController.get_by_cpf(cpf))

    usuariosController.delete(cpf)
    
def teste_delete():
    usuario = Usuario("Teste", "teste", 20, "123456", cpf, "Usuario")

    print(usuariosController.create(usuario))

    print(usuariosController.get_by_cpf(cpf))
    
    print(usuariosController.delete(cpf))

    print(usuariosController.get_by_cpf(cpf))


print("---------------------------CREATE---------------------------")
teste_create()
print("---------------------------DELETE---------------------------")
teste_delete()
print("---------------------------UPDATE---------------------------")
teste_update()

print("[FIM]")