import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '...')))
from src.models.Disco import Disco
from src.controllers.DiscosController import DiscosController
from datetime import datetime

discosController = DiscosController()
codigo_disco = 100000

def teste_create():
    disco = Disco(codigo_disco, 100000,100000, "Teste", datetime(2023, 1, 1), "Diretor Teste", 18)

    print(discosController.create(disco))
    print(discosController.get_by_codigo(codigo_disco))
    discosController.delete(codigo_disco)

def teste_update():
    disco = Disco(codigo_disco, 100000,100000, "Teste", datetime(2023, 1, 1), "Diretor Teste", 18)

    print(discosController.create(disco))

    print(discosController.get_by_codigo(codigo_disco))

    disco = Disco(codigo_disco, 100001,100001, "Teste Atualizado", datetime(2023, 1, 2), "Diretor Atualizado", 16)

    print(discosController.update(disco))

    print(discosController.get_by_codigo(codigo_disco))

    discosController.delete(codigo_disco)
    
def teste_delete():
    disco = Disco(codigo_disco, 100000,100000, "Teste", datetime(2023, 1, 1), "Diretor Teste", 18)

    print(discosController.create(disco))

    print(discosController.get_by_codigo(codigo_disco))

    print(discosController.delete(codigo_disco))

    print(discosController.get_by_codigo(codigo_disco))


print("---------------------------CREATE---------------------------")
teste_create()
print("---------------------------DELETE---------------------------")
teste_delete()
print("---------------------------UPDATE---------------------------")
teste_update()

print("[FIM]")