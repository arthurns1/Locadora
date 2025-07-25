import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QVBoxLayout, QWidget, QStackedWidget, QGridLayout, QPushButton, QLineEdit, QListWidget, QPlainTextEdit, QMessageBox)
from PyQt5.QtCore import Qt

from controllers.UsuariosController import UsuariosController
from controllers.SessaoController import SessaoController
from controllers.DiscosController import DiscosController
from controllers.GenerosController import GenerosController
from controllers.EmprestimosController import EmprestimosController
from controllers.EmprestimoDiscoController import EmprestimoDiscoController

from models.Usuario import Usuario
from models.Sessao import Sessao
from models.Disco import Disco
from models.Genero import Genero
from models.Emprestimo import Emprestimo  
from models.EmprestimoDisco import EmprestimoDisco

from functions.show_warning_message_box import show_warning_message_box

import datetime

sessaoController = SessaoController()
usuariosController = UsuariosController()
discosController = DiscosController()
generosController = GenerosController()
emprestimosController = EmprestimosController()
emprestimoDiscoController = EmprestimoDiscoController()

usuario_atual = Usuario("", "", -1, "", "", "")
body = {}

class Login(QWidget):    
    def __init__(self, stacked_widget: QStackedWidget):
        super().__init__()

        self.titleLogin = QLabel("Login:")
        self.login = QLineEdit()
        self.titleSenha = QLabel("Senha:")
        self.senha = QLineEdit()
        self.loginButton = QPushButton("Logar")
        self.loginButton.clicked.connect(lambda: self.handleLogin())
        
        self.stacked_widget = stacked_widget

        
        self.initUI()   

    def initUI(self):
        layout = QGridLayout()

        self.titleLogin.setGeometry(0, 0, self.width(), 40)

        self.titleLogin.setAlignment(Qt.AlignCenter)
        
        self.titleSenha.setGeometry(0, 0, self.width(), 40)

        self.titleSenha.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.titleLogin, 0, 0)

        layout.addWidget(self.login, 0, 1)
        
        layout.addWidget(self.titleSenha, 1, 0)

        layout.addWidget(self.senha, 1, 1)
        
        layout.addWidget(self.loginButton, 2,0)

        self.setLayout(layout)

    def check_info(self):

        self.usuario = usuariosController.get_by_login(self.login.text())
        
        if len(self.usuario) == 0:
            show_warning_message_box("Usuário não encontrado")
            return False

        if self.usuario[0][1] != self.senha.text():
            show_warning_message_box("Senha incorreta")
            return False

        return True

    def handleLogin(self):      
        if self.check_info():
            global usuario_atual
            usuario_atual = Usuario(self.usuario[0][1], self.usuario[0][2], self.usuario[0][3], self.usuario[0][4], self.usuario[0][0], self.usuario[0][5])
            self.stacked_widget.setCurrentIndex(3)

class Register(QWidget):
    def __init__(self, stacked_widget: QStackedWidget):
        super().__init__()

        self.stacked_widget = stacked_widget
        
        self.title1 = QLabel("Login:")
        self.login = QLineEdit()
        self.title2 = QLabel("Senha:")
        self.senha = QLineEdit()
        self.title3 = QLabel("Nome:")
        self.nome = QLineEdit()
        self.title4 = QLabel("idade:")
        self.idade = QLineEdit()
        self.title5 = QLabel("CPF:")
        self.cpf = QLineEdit()
        self.registerButton = QPushButton("Registrar")

        self.registerButton.clicked.connect(lambda: self.handleRegister())

        self.initUI()

    def initUI(self):
        layout = QGridLayout()

        layout.addWidget(self.title1,0 ,0)
        layout.addWidget(self.login, 0, 1)
        layout.addWidget(self.title2, 1, 0)
        layout.addWidget(self.senha, 1, 1)        
        layout.addWidget(self.title3,2 ,0)
        layout.addWidget(self.nome, 2, 1)
        layout.addWidget(self.title4, 3, 0)
        layout.addWidget(self.idade, 3, 1)        
        layout.addWidget(self.title5,4 ,0)
        layout.addWidget(self.cpf, 4, 1)
        layout.addWidget(self.registerButton, 7, 0)        
        
        self.setLayout(layout)

    def handleRegister(self):
        nome = self.nome.text()
        login = self.login.text()
        idade = self.idade.text() 
        senha = self.senha.text()
        cpf = self.cpf.text()

        if self.check_info(nome, login, idade, senha, cpf):
            usuario = Usuario(nome, login, int(idade), senha, cpf, "")
            usuariosController.create(usuario)

        self.stacked_widget.setCurrentIndex(0)    
        
    def check_info(self, nome, login, idade, senha, cpf):
        if len(nome) < 3:
            show_warning_message_box("Nome muito curto")
            return False

        if len(login) < 3:
            show_warning_message_box("Login muito curto")
            return False

        if usuariosController.get_by_login(login):
            show_warning_message_box("Este login já existe")
            return False
        
        if len(senha) < 3: 
            show_warning_message_box("Senha muito curta")
            return False

        if len(idade) <= 0:
            show_warning_message_box("Idade inválida")
            return False 
    
        if len(cpf) != 11 or usuariosController.get_by_cpf(cpf):
            show_warning_message_box("Insira um CPF válido")
            return False

        return True

class Funcionarios(QWidget):
    def __init__(self, stacked_widget:QStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.voltar = QPushButton("Voltar")
        self.adicionarFuncionario = QPushButton("Adicionar Funcionário")
        self.listarFuncionarios = QPushButton("Listar Funcionários")

        self.voltar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))
        self.adicionarFuncionario.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(5))
        self.listarFuncionarios.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(6))
        
        self.initUI()

    def initUI(self):
        layout = QGridLayout()

        layout.addWidget(self.adicionarFuncionario, 0, 0)
        layout.addWidget(self.listarFuncionarios, 1, 0)

        self.setLayout(layout)
 
class AdicionarFuncionario(QWidget):
    def __init__(self, stacked_widget: QStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget

        self.voltar = QPushButton("Voltar")
        self.titleCpf = QLabel("CPF:")
        self.cpf = QLineEdit()
        self.titleNome = QLabel("Nome:")
        self.nome = QLineEdit()
        self.titleLogin = QLabel("Login:")
        self.login = QLineEdit()
        self.titleIdade = QLabel("Idade:")
        self.idade = QLineEdit()
        self.titleSenha = QLabel("Senha:")
        self.senha = QLineEdit()
        self.titleCargo = QLabel("Cargo:")
        self.cargo = QListWidget()
        self.adicionar = QPushButton("Adicionar")
        
        self.adicionar.clicked.connect(self.handle_adicionar)
        self.voltar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))

        self.initUI() 

    def validate_inputs(self):
        if not self.cpf.text() or not self.nome.text() or not self.login.text() or not self.idade.text() or not self.senha.text() or not self.cargo.currentItem():
            return False
        return True

    def handle_adicionar(self):
        if not self.validate_inputs():
            return

        funcionario = Usuario(
            cpf=self.cpf.text(),
            nome=self.nome.text(),
            login=self.login.text(),
            idade=self.idade.text(),
            senha=self.senha.text(),
            cargo=self.cargo.currentItem().text()
        )
        
        usuariosController.create(funcionario)

        self.stacked_widget.setCurrentIndex(3)
        
    def initUI(self):
        layout = QGridLayout()

        self.cargo.addItem("Funcionario")
        self.cargo.addItem("Admin")
        
        layout.addWidget(self.voltar, 0, 0)
        layout.addWidget(self.titleCpf, 1, 0)
        layout.addWidget(self.cpf, 1, 1)
        layout.addWidget(self.titleNome, 2, 0)
        layout.addWidget(self.nome, 2, 1)
        layout.addWidget(self.titleLogin, 3, 0)
        layout.addWidget(self.login, 3, 1)
        layout.addWidget(self.titleIdade, 4, 0)
        layout.addWidget(self.idade, 4, 1)
        layout.addWidget(self.titleSenha, 5, 0)
        layout.addWidget(self.senha, 5, 1)
        layout.addWidget(self.titleCargo, 6, 0)
        layout.addWidget(self.cargo, 6, 1)
        layout.addWidget(self.adicionar, 7, 0)  
        self.setLayout(layout)

class ListarFuncionario(QWidget):
    def __init__(self, stacked_widget: QStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget

        self.voltar = QPushButton("Voltar")
        self.recarregar = QPushButton("Recarregar")

        self.recarregar.clicked.connect(self.carregar_lista)
        
        self.funcionarios = usuariosController.get_all()
        self.title = QLabel("Listar Funcionários")
        self.lista = QListWidget()
        self.remover = QPushButton("Remover")
        self.editar = QPushButton("Editar")
        
        self.remover.clicked.connect(self.handle_remover)
        self.editar.clicked.connect(self.handle_editar)
        
        self.voltar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))
        
        self.initUI()

    def initUI(self):
        layout = QGridLayout()

        self.carregar_lista()

        layout.addWidget(self.recarregar, 0, 1)        
        layout.addWidget(self.voltar, 0, 0)
        layout.addWidget(self.title, 1, 0)
        layout.addWidget(self.lista, 2, 0)
        layout.addWidget(self.remover, 3, 0)
        layout.addWidget(self.editar, 3, 1)

        self.setLayout(layout)

    def handle_remover(self):
        item = self.lista.currentItem()
        if item:
            cpf = item.text().split(" - ")[1]
            usuariosController.delete(cpf)
            self.carregar_lista()

    def handle_editar(self):
        item = self.lista.currentItem()
        if item:
            body["funcionario"] = item.text().split(" - ")[1]
            self.stacked_widget.setCurrentIndex(7)

    def carregar_lista(self):
        self.lista.clear()
        funcionarios = usuariosController.get_all()
        for funcionario in funcionarios:
            if funcionario[5] == "Funcionario":
                self.lista.addItem(funcionario[4] + " - " + funcionario[0])

class EditarFuncionario(QWidget):
    def __init__(self, stacked_widget: QStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget

        self.voltar = QPushButton("Voltar")
        self.titleCpf = QLabel("CPF:")
        self.cpf = QLineEdit()
        self.titleNome = QLabel("Nome:")
        self.nome = QLineEdit()
        self.titleLogin = QLabel("Login:")
        self.login = QLineEdit()
        self.titleIdade = QLabel("Idade:")
        self.idade = QLineEdit()
        self.titleSenha = QLabel("Senha:")
        self.senha = QLineEdit()
        self.titleCargo = QLabel("Cargo:")
        self.cargo = QListWidget()
        self.editar = QPushButton("Editar")

        self.cargo.addItem("Funcionario")
        self.cargo.addItem("Admin")
        
        self.editar.clicked.connect(self.handle_editar)
        self.voltar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))

        self.initUI()

    def initUI(self):
        layout = QGridLayout()

        layout.addWidget(self.voltar, 0, 0)
        layout.addWidget(self.titleCpf, 1, 0)
        layout.addWidget(self.cpf, 1, 1)
        layout.addWidget(self.titleNome, 2, 0)
        layout.addWidget(self.nome, 2, 1)
        layout.addWidget(self.titleLogin, 3, 0)
        layout.addWidget(self.login, 3, 1)
        layout.addWidget(self.titleIdade, 4, 0)
        layout.addWidget(self.idade, 4, 1)
        layout.addWidget(self.titleSenha, 5, 0)
        layout.addWidget(self.senha, 5, 1)
        layout.addWidget(self.titleCargo, 6, 0)
        layout.addWidget(self.cargo, 6, 1)
        layout.addWidget(self.editar, 7, 0)
        
        self.setLayout(layout)

    def handle_editar(self):
        if body["funcionario"]:    
            funcionario = Usuario(
                cpf=body["funcionario"],
                nome=self.nome.text(),
                login=self.login.text(),
                idade=self.idade.text(),
                senha=self.senha.text(),
                cargo=self.cargo.currentItem().text()
            )
            
            usuariosController.update(funcionario)

            self.stacked_widget.setCurrentIndex(3)    

class Sessoes(QWidget):
    def __init__(self, stacked_widget: QStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget
        
        self.voltar = QPushButton("Voltar")
        self.adicionar = QPushButton("Adicionar Sessão")
        self.listar = QPushButton("Listar Sessões")

        self.voltar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))
        self.adicionar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(9))
        self.listar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(10))

        self.initUI()

    def initUI(self):
        layout = QGridLayout()

        layout.addWidget(self.voltar, 0, 0)
        layout.addWidget(self.adicionar, 1, 0)
        layout.addWidget(self.listar, 2, 0)
        self.setLayout(layout)  

class AdicionarSessao(QWidget):
    def __init__(self, stacked_widget: QStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget

        self.voltar = QPushButton("Voltar")
        self.titleCorredor = QLabel("Corredor:")
        self.corredor = QLineEdit()
        self.adicionar = QPushButton("Adicionar")

        self.adicionar.clicked.connect(self.handle_adicionar)
        self.voltar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))

        self.initUI()

    def handle_adicionar(self):
        sessao = Sessao(0, self.corredor.text())
        
        if sessao:
            sessaoController.create(sessao)
            self.stacked_widget.setCurrentIndex(3)

    def initUI(self):
        layout = QGridLayout()  

        layout.addWidget(self.voltar, 0, 0)
        layout.addWidget(self.titleCorredor, 1, 0)
        layout.addWidget(self.corredor, 1, 1)
        layout.addWidget(self.adicionar, 2, 0)

        self.setLayout(layout)

class ListarSessoes(QWidget):
    def __init__(self, stacked_widget: QStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget

        self.voltar = QPushButton("Voltar")
        self.recarregar = QPushButton("Recarregar")

        self.recarregar.clicked.connect(self.carregar_lista)
        
        self.title = QLabel("Listar Sessões")
        self.lista = QListWidget()
        self.remover = QPushButton("Remover")
        self.editar = QPushButton("Editar")
        
        self.remover.clicked.connect(self.handle_remover)
        self.editar.clicked.connect(self.handle_editar)
        
        self.voltar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))
        
        self.initUI()

    def initUI(self):
        layout = QGridLayout()

        self.carregar_lista()

        layout.addWidget(self.recarregar, 0, 1)        
        layout.addWidget(self.voltar, 0, 0)
        layout.addWidget(self.title, 1, 0)
        layout.addWidget(self.lista, 2, 0)
        layout.addWidget(self.remover, 3, 0)
        layout.addWidget(self.editar, 3, 1)
        self.setLayout(layout)

    def handle_remover(self):
        item = self.lista.currentItem()
        if item:
            numero = int(item.text().split(" - ")[1])
            sessaoController.delete(numero)
            self.carregar_lista()

    def handle_editar(self):
        item = self.lista.currentItem()
        if item:
            numero = int(item.text().split(" - ")[1])
            body["sessao"] = numero
            self.stacked_widget.setCurrentIndex(11)

    def carregar_lista(self):
        self.lista.clear()
        sessoes = sessaoController.get_all()
        for sessao in sessoes:
            self.lista.addItem(sessao[0] + " - " + str(sessao[1]))

class EditarSessao(QWidget):
    def __init__(self, stacked_widget: QStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget

        self.voltar = QPushButton("Voltar")
        self.titleCorredor = QLabel("Corredor:")
        self.corredor = QLineEdit()
        self.editar = QPushButton("Editar")
        
        self.editar.clicked.connect(self.handle_editar)
        self.voltar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))

        self.initUI()

    def handle_editar(self):
        if body["sessao"]:
            sessao = Sessao(body["sessao"], self.corredor.text())
            sessaoController.update(sessao)
            self.stacked_widget.setCurrentIndex(3)

    def initUI(self):
        layout = QGridLayout()  

        layout.addWidget(self.voltar, 0, 0)
        layout.addWidget(self.titleCorredor, 1, 0)
        layout.addWidget(self.corredor, 1, 1)
        layout.addWidget(self.editar, 2, 0)

        self.setLayout(layout)

class Discos(QWidget):
    def __init__(self, stacked_widget:QStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget
        
        self.voltar = QPushButton("Voltar")
        self.adicionar = QPushButton("Adicionar Discos")
        self.listar = QPushButton("Listar Discos")

        self.voltar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))
        self.adicionar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(13))
        self.listar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(14))
        self.initUI()

    def initUI(self):
        layout = QGridLayout()

        layout.addWidget(self.voltar, 0, 0)
        layout.addWidget(self.adicionar, 1, 0)
        layout.addWidget(self.listar, 2, 0)
        self.setLayout(layout)

class AdicionarDiscos(QWidget):
    def __init__(self, stacked_widget: QStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.voltar = QPushButton("Voltar")
        self.recarregar = QPushButton("Recarregar")

        self.recarregar.clicked.connect(self.handle_recarregar)
        self.voltar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))
        
        self.titleTitulo = QLabel("Título:")
        self.titulo = QLineEdit()
        self.titleDiretor = QLabel("Diretor:")
        self.diretor = QLineEdit()
        self.titleLancamento = QLabel("Lançamento:")
        self.lancamento = QLineEdit()
        self.titleClassInd = QLabel("Classificação Indicativa:")
        self.class_ind = QLineEdit()
        self.titleSessao = QLabel("Sessão:")
        self.sessao = QListWidget()
        self.titleGenero = QLabel("Gênero:")
        self.genero = QListWidget()
        self.adicionar = QPushButton("Adicionar")

        self.carregar_generos()
        self.carregar_sessoes()
        
        self.initUI()

    def initUI(self):
        layout = QGridLayout()

        layout.addWidget(self.voltar, 0, 0)
        layout.addWidget(self.recarregar, 0, 1)
        layout.addWidget(self.titleTitulo, 1, 0)
        layout.addWidget(self.titulo, 1, 1)
        layout.addWidget(self.titleDiretor, 2, 0)
        layout.addWidget(self.diretor, 2, 1)
        layout.addWidget(self.titleLancamento, 3, 0)
        layout.addWidget(self.lancamento, 3, 1)
        layout.addWidget(self.titleClassInd, 4, 0)
        layout.addWidget(self.class_ind, 4, 1)
        layout.addWidget(self.titleSessao, 5, 0)
        layout.addWidget(self.sessao, 5, 1)
        layout.addWidget(self.titleGenero, 6, 0)
        layout.addWidget(self.genero, 6, 1)
        layout.addWidget(self.adicionar, 7, 0)  

        self.adicionar.clicked.connect(self.handle_adicionar)
        
        self.setLayout(layout)

    def handle_adicionar(self):
        disco = Disco(
            codigo=0,
            titulo=self.titulo.text(),
            diretor=self.diretor.text(),
            lancamento=self.lancamento.text(),
            classInd=self.class_ind.text(),
            codigoGenero= self.genero.currentItem().text().split(" - ")[0],
            numSessao=self.sessao.currentItem().text().split(" - ")[0],
        )

        if disco:
            discosController.create(disco)

            self.stacked_widget.setCurrentIndex(3)

    def handle_recarregar(self):
        self.sessao.clear()
        self.genero.clear()
        self.carregar_sessoes()
        self.carregar_generos()
        
    def carregar_sessoes(self):
        sessoes = sessaoController.get_all()
        for sessao in sessoes:
            self.sessao.addItem(str(sessao[1]) + " - " + sessao[0])

    def carregar_generos(self):
        generos = generosController.get_all()
        for genero in generos:
            self.genero.addItem(str(genero[0]) + " - " + genero[2])

class ListarDiscos(QWidget):
    def __init__(self, stacked_widget: QStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget
        
        self.voltar = QPushButton("Voltar")
        self.recarregar = QPushButton("Recarregar")

        self.voltar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))
        self.recarregar.clicked.connect(self.carregar_discos)
        
        self.titleLista = QLabel("Discos:")
        self.lista = QListWidget()        
        self.remover = QPushButton("Remover")
        self.editar = QPushButton("Editar")

        self.remover.clicked.connect(self.handle_remover)
        self.editar.clicked.connect(self.handle_editar)
        
        self.initUI()

    def initUI(self):
        layout = QGridLayout()

        self.carregar_discos()
        
        layout.addWidget(self.voltar, 0, 0)
        layout.addWidget(self.recarregar, 0, 1)
        layout.addWidget(self.titleLista, 1, 0)
        layout.addWidget(self.lista, 2, 0)
        layout.addWidget(self.remover, 3, 0)
        layout.addWidget(self.editar, 3, 1)
        
        self.setLayout(layout)

    def handle_remover(self):
        item = self.lista.currentItem()
        if item:
            codigo_disco = item.text().split(" - ")[0]
            discosController.delete(int(codigo_disco))
            self.carregar_discos()

    def handle_editar(self):
        item = self.lista.currentItem()

        if item:
            numero = item.text().split(" - ")[0]
            body["disco"] = numero
            self.stacked_widget.setCurrentIndex(15)

    def carregar_discos(self):
        self.lista.clear()
        discos = discosController.get_all()

        for disco in discos:
            self.lista.addItem(str(disco[0]) + " - " + disco[3])

class EditarDiscos(QWidget):
    def __init__(self, stacked_widget: QStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.voltar = QPushButton("Voltar")
        self.recarregar = QPushButton("Recarregar")

        self.recarregar.clicked.connect(self.handle_recarregar)
        self.voltar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))
        
        self.titleTitulo = QLabel("Título:")
        self.titulo = QLineEdit()
        self.titleDiretor = QLabel("Diretor:")
        self.diretor = QLineEdit()
        self.titleLancamento = QLabel("Lançamento:")
        self.lancamento = QLineEdit()
        self.titleClassInd = QLabel("Classificação Indicativa:")
        self.class_ind = QLineEdit()
        self.titleSessao = QLabel("Sessão:")
        self.sessao = QListWidget()
        self.titleGenero = QLabel("Gênero:")
        self.genero = QListWidget()
        self.editar = QPushButton("Editar")

        self.carregar_generos()
        self.carregar_sessoes()
        
        self.initUI()

    def initUI(self):
        layout = QGridLayout()

        layout.addWidget(self.voltar, 0, 0)
        layout.addWidget(self.recarregar, 0, 1)
        layout.addWidget(self.titleTitulo, 1, 0)
        layout.addWidget(self.titulo, 1, 1)
        layout.addWidget(self.titleDiretor, 2, 0)
        layout.addWidget(self.diretor, 2, 1)
        layout.addWidget(self.titleLancamento, 3, 0)
        layout.addWidget(self.lancamento, 3, 1)
        layout.addWidget(self.titleClassInd, 4, 0)
        layout.addWidget(self.class_ind, 4, 1)
        layout.addWidget(self.titleSessao, 5, 0)
        layout.addWidget(self.sessao, 5, 1)
        layout.addWidget(self.titleGenero, 6, 0)
        layout.addWidget(self.genero, 6, 1)
        layout.addWidget(self.editar, 7, 0)  

        self.editar.clicked.connect(self.handle_editar)
        
        self.setLayout(layout)

    def handle_editar(self):
        if body["disco"]:
                
            disco = Disco(
                codigo=body["disco"],
                titulo=self.titulo.text(),
                diretor=self.diretor.text(),
                lancamento=self.lancamento.text(),
                classInd=self.class_ind.text(),
                codigoGenero= self.genero.currentItem().text().split(" - ")[0],
                numSessao=self.sessao.currentItem().text().split(" - ")[0],
                emprestado=False
            )
            if disco:
                discosController.update(disco)
                self.stacked_widget.setCurrentIndex(3)

    def handle_recarregar(self):
        self.sessao.clear()
        self.genero.clear()
        self.carregar_sessoes()
        self.carregar_generos()
        
    def carregar_sessoes(self):
        sessoes = sessaoController.get_all()
        for sessao in sessoes:
            self.sessao.addItem(str(sessao[1]) + " - " + sessao[0])

    def carregar_generos(self):
        generos = generosController.get_all()
        for genero in generos:
            self.genero.addItem(str(genero[0]) + " - " + genero[2])

class Generos(QWidget):
    def __init__(self, stacked_widget: QStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.voltar = QPushButton("Voltar")

        self.voltar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))
        
        self.adicionar = QPushButton("Adicionar Gênero")

        self.adicionar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(17))
        
        self.listar = QPushButton("Listar Gêneros")

        self.listar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(18))
        
        self.initUI()

    def initUI(self):
        layout = QGridLayout()

        layout.addWidget(self.voltar, 0, 0)
        layout.addWidget(self.adicionar, 1, 0)
        layout.addWidget(self.listar, 2, 0)
        
        self.setLayout(layout)

class AdicionarGeneros(QWidget):
    def __init__(self, stacked_widget: QStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget

        self.voltar = QPushButton("Voltar")

        self.voltar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))

        self.titleGenero = QLabel("Nome:")
        self.genero = QLineEdit()
        self.titleDescricao = QLabel("Descrição:")
        self.descricao = QPlainTextEdit()

        self.adicionar = QPushButton("Adicionar")

        self.adicionar.clicked.connect(self.handle_adicionar)

        self.initUI()

    def initUI(self):
        layout = QGridLayout()

        layout.addWidget(self.voltar, 0, 0)
        layout.addWidget(self.titleGenero, 1, 0)
        layout.addWidget(self.genero, 1, 1)
        layout.addWidget(self.titleDescricao, 2, 0)
        layout.addWidget(self.descricao, 2, 1)
        layout.addWidget(self.adicionar, 3, 0)

        self.setLayout(layout)

    def handle_adicionar(self):
        genero = Genero(0, self.genero.text(), self.descricao.toPlainText())

        if genero:
            generosController.create(genero)
        
        self.stacked_widget.setCurrentIndex(3)

class ListarGeneros(QWidget):
    def __init__(self, stacked_widget: QStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget

        self.voltar = QPushButton("Voltar")
        self.recarregar = QPushButton("Recarregar")

        self.voltar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))
        self.recarregar.clicked.connect(self.carregar_lista)
        
        self.title = QLabel("Listar Gêneros")
        self.lista = QListWidget()
        self.remover = QPushButton("Remover")
        self.editar = QPushButton("Editar")
                
        self.remover.clicked.connect(self.handle_remover)
        self.editar.clicked.connect(self.handle_editar)
        
        self.initUI()

    def initUI(self):
        layout = QGridLayout()

        self.carregar_lista()

        layout.addWidget(self.recarregar, 0, 1)        
        layout.addWidget(self.voltar, 0, 0)
        layout.addWidget(self.title, 1, 0)
        layout.addWidget(self.lista, 2, 0)
        layout.addWidget(self.remover, 3, 0)
        layout.addWidget(self.editar, 3, 1)
        self.setLayout(layout)

    def handle_remover(self):
        item = self.lista.currentItem()
        if item:
            codigo_genero = int(item.text().split(" - ")[1])
            generosController.delete(codigo_genero)
            self.carregar_lista()

    def handle_editar(self):
        item = self.lista.currentItem()
        if item:
            codigo_genero = int(item.text().split(" - ")[1])
            body["genero"] = codigo_genero
            self.stacked_widget.setCurrentIndex(19)
    
    def carregar_lista(self):
        self.lista.clear()
        generos = generosController.get_all()
        for genero in generos:
            self.lista.addItem(genero[2] + " - " + str(genero[0]))

class EditarGeneros(QWidget):
    def __init__(self, stacked_widget: QStackedWidget):
        super().__init__()
        
        self.stacked_widget = stacked_widget
        
        self.voltar = QPushButton("Voltar")

        self.voltar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))

        self.titleNome = QLabel("Nome:")
        self.nome = QLineEdit()
        self.titleDescricao = QLabel("Descrição:")
        self.descricao = QPlainTextEdit()

        self.adicionar = QPushButton("Editar")

        self.adicionar.clicked.connect(self.handle_editar)

        self.initUI()

    def initUI(self):
        layout = QGridLayout()

        layout.addWidget(self.voltar, 0, 0)
        layout.addWidget(self.titleNome, 1, 0)
        layout.addWidget(self.nome, 1, 1)
        layout.addWidget(self.titleDescricao, 2, 0)
        layout.addWidget(self.descricao, 2, 1)
        layout.addWidget(self.adicionar, 3, 0)

        self.setLayout(layout)

    def handle_editar(self):
        if body["genero"]:
            genero = Genero(body["genero"], self.nome.text(), self.nome.text())
            generosController.update(genero)
            self.stacked_widget.setCurrentIndex(3)

class Emprestimos(QWidget):
    def __init__(self, stacked_widget:QStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget
        
        self.voltar = QPushButton("Voltar")
        
        self.voltar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))
        
        self.fazer_emprestimo = QPushButton("Fazer empréstimo")
        self.realizar_devolucao = QPushButton("Realizar devolução")
        
        self.fazer_emprestimo.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(21))
        self.realizar_devolucao.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(22))
         
        self.initUI()
        
    def initUI(self):
        layout = QGridLayout()

        layout.addWidget(self.voltar, 0, 0)
        layout.addWidget(self.fazer_emprestimo, 1, 0)
        layout.addWidget(self.realizar_devolucao, 2, 0)

        self.setLayout(layout)

class RealizarEmprestimo(QWidget):
    def __init__(self, stacked_widget: QStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget

        self.recarregar = QPushButton("Recarregar")
        self.voltar = QPushButton("Voltar")
        
        self.voltar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))
        self.recarregar.clicked.connect(self.carregar_disco)
        
        self.titleDiscos = QLabel("Discos:")
        self.discos = QListWidget()

        self.discos.setSelectionMode(QListWidget.ExtendedSelection)
        self.emprestimo = QPushButton("Realizar Empréstimo")

        self.emprestimo.clicked.connect(self.handle_emprestimo)
        
        self.initUI()

    def handle_emprestimo(self):
        quant_discos = len(emprestimoDiscoController.get_emprestimo_disco_by_usuario(usuario_atual.get_cpf()))

        if len(self.discos.selectedItems()) + quant_discos <= 3:
            emprestimo = Emprestimo(
                cpfCliente=usuario_atual.get_cpf(),
                codEmprestimo=0,
                dataEmprestimo=datetime.datetime.now(),
                prazo=datetime.datetime.today() + datetime.timedelta(days=7)
            )

            codigo_emprestimo = emprestimosController.create(emprestimo=emprestimo)[0][0]
        
            for disco in self.discos.selectedItems():
                codigo_disco = disco.text().split(" - ")[1]

                emprestimo_disco = EmprestimoDisco(codigo_disco, codigo_emprestimo)

                emprestimoDiscoController.create(emprestimo_disco)

            self.carregar_disco()

            self.stacked_widget.setCurrentIndex(3)

            return True
        show_warning_message_box("Só é permitido o empréstimo de no MÁXIMO 3 discos")
        self.stacked_widget.setCurrentIndex(3)
        
        return False

    def initUI(self):
        layout = QGridLayout()

        self.carregar_disco()
        
        layout.addWidget(self.voltar, 0, 0)
        layout.addWidget(self.recarregar, 0, 1)
        layout.addWidget(self.titleDiscos, 1, 0)
        layout.addWidget(self.discos, 2, 0)
        layout.addWidget(self.emprestimo, 3, 0)
        
        self.setLayout(layout)

    def carregar_disco(self):
        self.discos.clear()
        discos = discosController.get_not_emprestados()

        for disco in discos:
            self.discos.addItem(disco[3] + " - " + str(disco[0]))

class RealizarDevolucao(QWidget):
    def __init__(self, stacked_widget: QStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget

        self.voltar = QPushButton("Voltar")
        
        self.voltar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))
        
        self.titleDiscos = QLabel("Discos:")
        self.discos = QListWidget()

        self.discos.setSelectionMode(QListWidget.ExtendedSelection)
        self.devolver = QPushButton("Devolver")

        self.devolver.clicked.connect(self.handle_devolver)
        
        self.initUI()

    def handle_devolver(self):
        if self.discos.selectedItems():
            for disco in self.discos.selectedItems():
                codigo_disco = disco.text().split(" - ")[1]
                emprestimoDiscoController.delete_by_disco(codigo_disco)
            
            self.carregar_disco()

            self.stacked_widget.setCurrentIndex(3)
    
    def initUI(self):
        layout = QGridLayout()

        self.carregar_disco()
        
        layout.addWidget(self.voltar, 0, 0)
        layout.addWidget(self.titleDiscos, 1, 0)
        layout.addWidget(self.discos, 2, 0)
        layout.addWidget(self.devolver, 3, 0)
        
        self.setLayout(layout)

    def carregar_disco(self):
        self.discos.clear()
        discos = discosController.get_discos_by_cpf(usuario_atual.get_cpf())

        for disco in discos:
            self.discos.addItem(disco[3] + " - " + str(disco[0]))


class Menu(QWidget):
    def __init__(self, stacked_widget: QStackedWidget):
        super().__init__()

        self.setWindowTitle("Locadora do Tonhão")
        self.setGeometry(0, 0, 500, 300)

        self.title1 = QLabel("Locadora do Tonho")
        self.loginButton = QPushButton("Login")
        self.registerButton = QPushButton("Registrar")

        self.loginButton.clicked.connect(lambda: stacked_widget.setCurrentIndex(1))
        self.registerButton.clicked.connect(lambda: stacked_widget.setCurrentIndex(2))
        
        self.initUI()            

    def initUI(self):

        layout = QGridLayout()

        self.title1.setGeometry(0 , 0, self.width(), 20)

        self.title1.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.title1, 0, 0)
        layout.addWidget(self.loginButton, 1, 0)
        layout.addWidget(self.registerButton, 2, 0)
        
        self.setLayout(layout)
          
class MenuLogin(QWidget):
    def __init__(self, stacked_widget:QStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget
        
        self.logout = QPushButton("Logout")
                
        self.emprestimo = QPushButton("Emprestimo")

        self.generos = QPushButton("Gerenciar Gêneros")

        self.sessao = QPushButton("Gerenciar Sessões")

        self.discos = QPushButton("Gerenciar Discos")

        self.funcionarios = QPushButton("Gerenciar Funcionários")

        self.logout.clicked.connect(self.handle_logout)
        self.discos.clicked.connect(self.handle_discos)
        self.emprestimo.clicked.connect(self.handle_emprestimos)
        self.sessao.clicked.connect(self.handle_sessao)
        self.funcionarios.clicked.connect(self.handle_funcionarios)
        self.generos.clicked.connect(self.handle_generos)

        self.initUI()

    def initUI(self):
        layout = QGridLayout()
            
        layout.addWidget(self.logout, 0, 0)
        layout.addWidget(self.discos, 1, 0)
        layout.addWidget(self.emprestimo, 2, 0)
        layout.addWidget(self.sessao, 3, 0)
        layout.addWidget(self.funcionarios, 4, 0)
        layout.addWidget(self.generos, 5, 0)
                
        self.setLayout(layout)

    def handle_logout(self):
        global usuario_atual
        usuario_atual = Usuario("", "", -1, "", "", "")
        self.stacked_widget.setCurrentIndex(0)

    def handle_discos(self):
        global usuario_atual
        if usuario_atual.get_cargo() == "Funcionario" or usuario_atual.get_cargo() == "Admin":
            self.stacked_widget.setCurrentIndex(12)
        else:
            show_warning_message_box("Acesso negado")
            
    def handle_emprestimos(self):
        global usuario_atual
        if usuario_atual.get_cargo() != "Funcionario":
            self.stacked_widget.setCurrentIndex(20)
        else:
            show_warning_message_box("Acesso negado")

    def handle_sessao(self):
        global usuario_atual
        if usuario_atual.get_cargo() == "Funcionario" or usuario_atual.get_cargo() == "Admin":
            self.stacked_widget.setCurrentIndex(8)
        else:
            show_warning_message_box("Acesso negado")

    def handle_funcionarios(self):
        global usuario_atual
        if usuario_atual.get_cargo() == "Admin":    
            self.stacked_widget.setCurrentIndex(4)
        else:
            show_warning_message_box("Acesso negado")

    def handle_generos(self):
        global usuario_atual
        if usuario_atual.get_cargo() == "Funcionario" or usuario_atual.get_cargo() == "Admin":
            self.stacked_widget.setCurrentIndex(16)
        else:
            show_warning_message_box("Acesso negado")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Locadora do Tonho")
        self.setGeometry(0, 0, 700, 450)
        self.setFixedSize(700, 500)
            
        self.stacked_widget = QStackedWidget()

        self.menuWindow = Menu(self.stacked_widget)
        self.loginWindow = Login(self.stacked_widget)
        self.registerWindow = Register(self.stacked_widget)
        self.menuLogin = MenuLogin(self.stacked_widget)

        self.funcionarios = Funcionarios(self.stacked_widget)
        self.adicionarFuncionario = AdicionarFuncionario(self.stacked_widget)
        self.listarFuncionario = ListarFuncionario(self.stacked_widget)
        self.editarFuncionario = EditarFuncionario(self.stacked_widget)
        
        self.sessoes = Sessoes(self.stacked_widget)
        self.adicionarSessao = AdicionarSessao(self.stacked_widget)
        self.listarSessoes = ListarSessoes(self.stacked_widget)
        self.editarSessoes = EditarSessao(self.stacked_widget)

        self.discos = Discos(self.stacked_widget)
        self.adicionarDiscos = AdicionarDiscos(self.stacked_widget)
        self.listarDiscos = ListarDiscos(self.stacked_widget)
        self.editarDiscos = EditarDiscos(self.stacked_widget)

        self.generos = Generos(self.stacked_widget)
        self.adicionarGeneros = AdicionarGeneros(self.stacked_widget)
        self.listarGeneros = ListarGeneros(self.stacked_widget)
        self.editarGeneros = EditarGeneros(self.stacked_widget)
        
        self.emprestimos = Emprestimos(self.stacked_widget)
        self.realizarEmprestimo = RealizarEmprestimo(self.stacked_widget)
        self.realizarDevolucao = RealizarDevolucao(self.stacked_widget)
        
        self.stacked_widget.addWidget(self.menuWindow)
        self.stacked_widget.addWidget(self.loginWindow)
        self.stacked_widget.addWidget(self.registerWindow)
        self.stacked_widget.addWidget(self.menuLogin)

        self.stacked_widget.addWidget(self.funcionarios)
        self.stacked_widget.addWidget(self.adicionarFuncionario)
        self.stacked_widget.addWidget(self.listarFuncionario)
        self.stacked_widget.addWidget(self.editarFuncionario)

        self.stacked_widget.addWidget(self.sessoes)
        self.stacked_widget.addWidget(self.adicionarSessao)
        self.stacked_widget.addWidget(self.listarSessoes)
        self.stacked_widget.addWidget(self.editarSessoes)
        
        self.stacked_widget.addWidget(self.discos)
        self.stacked_widget.addWidget(self.adicionarDiscos)
        self.stacked_widget.addWidget(self.listarDiscos)
        self.stacked_widget.addWidget(self.editarDiscos)

        self.stacked_widget.addWidget(self.generos)
        self.stacked_widget.addWidget(self.adicionarGeneros)
        self.stacked_widget.addWidget(self.listarGeneros)
        self.stacked_widget.addWidget(self.editarGeneros)

        self.stacked_widget.addWidget(self.emprestimos)
        self.stacked_widget.addWidget(self.realizarEmprestimo)
        self.stacked_widget.addWidget(self.realizarDevolucao)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stacked_widget)
        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
