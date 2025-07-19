import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QStackedWidget, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from controllers.UsuariosController import UsuariosController
from models.Usuario import Usuario

usuariosController = UsuariosController()
usuario_atual = Usuario("", "", -1, "", "", "")


class Login(QWidget):
    def __init__(self, stacked_widget: QStackedWidget):
        super().__init__()

        self.titleLogin = QLabel("Login:")
        self.login = QLineEdit()
        self.titleSenha = QLabel("Senha:")
        self.senha = QLineEdit()
        self.error = QLabel()
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

        layout.addWidget(self.error, 2, 0)
        
        layout.addWidget(self.loginButton, 3,0)

        self.setLayout(layout)

    def check_info(self):

        self.usuario = usuariosController.get_by_login(self.login.text())
        
        if len(self.usuario) == 0:
            self.show_error_message("Usuário não encontrado")
            return False

        if self.usuario[0][4] != self.senha.text():
            self.show_error_message("Senha incorreta")
            return False

        return True

    def show_error_message(self, error_message:str):
        self.error.setText(error_message)

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
        self.error = QLabel()
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
        layout.addWidget(self.error, 6, 1)
        layout.addWidget(self.registerButton, 7, 0)        
        
        self.setLayout(layout)

    def handleRegister(self):
        nome = self.nome.text()
        login = self.login.text()
        idade = self.idade.text() 
        senha = self.senha.text()
        cpf = self.cpf.text()

        if self.check_info(nome, login, idade, senha, cpf):
            usuario = Usuario(nome, login, int(idade), senha, cpf, "Usuário")
            usuariosController.create(usuario)

        self.stacked_widget.setCurrentIndex(0)    
        
    def check_info(self, nome, login, idade, senha, cpf):
        if len(nome) < 3:
            self.show_error_message("Nome muito curto")
            return False

        if len(login) < 3:
            self.show_error_message("Login muito curto")
            return False

        if len(senha) < 3: 
            self.show_error_message("Login muito curto")
            return False

        if len(idade) <= 0:
            self.show_error_message("Idade inválida")
            return False 
    
        if len(cpf) != 11:
            self.show_error_message("Insira um CPF válido")
            return False

        return True

    def show_error_message(self, error_message:str):
        self.error.setText(error_message)

class Funcionarios(QWidget):
    def __init__(self, stacked_widget:QStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget

        self.voltar = QPushButton("Voltar")
        self.adicionar = QPushButton("Adicionar Funcionário")
        self.listar = QPushButton("Listar Funcionários")
        self.editar = QPushButton("Editar Funcionario")
        self.remover = QPushButton("Remover Funcionário")
        
        self.initUI()

    def initUI(self):
        layout = QGridLayout()

        layout.addWidget(self.voltar, 0, 0)
        layout.addWidget(self.adicionar, 1, 0)
        layout.addWidget(self.listar, 2, 0)
        layout.addWidget(self.editar, 3, 0)
        layout.addWidget(self.remover, 4, 0)
        self.setLayout(layout)

    def handle_voltar(self):
        self.stacked_widget.setCurrentIndex(3)

class Discos(QWidget):
    def __init__(self, stacked_widget:QStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget
        
        self.voltar = QPushButton("Voltar")
        self.adicionar = QPushButton("Adicionar Disco")
        self.listar = QPushButton("Listar Disco")
        self.editar = QPushButton("Editar Disco")
        self.remover = QPushButton("Remover Disco")

        self.voltar.clicked.connect(self.handle_voltar)
        self.initUI()

    def initUI(self):
        layout = QGridLayout()

        layout.addWidget(self.voltar, 0, 0)
        layout.addWidget(self.adicionar, 1, 0)
        layout.addWidget(self.listar, 2, 0)
        layout.addWidget(self.editar, 3, 0)
        layout.addWidget(self.remover, 4, 0)
        self.setLayout(layout)

    def handle_voltar(self):
        self.stacked_widget.setCurrentIndex(3)

class Emprestimos(QWidget):
    def __init__(self, stacked_widget:QStackedWidget):
        super().__init__()
        self.stacked_widget = stacked_widget
        
        self.voltar = QPushButton("Voltar")
        self.adicionar = QPushButton("Fazer empréstimo")
        self.listar = QPushButton("Listar empréstimos")

    def initUI(self):
        layout = QGridLayout()

        layout.addWidget(self.voltar, 0, 0)
        layout.addWidget(self.adicionar, 1, 0)
        layout.addWidget(self.listar, 2, 0)
        self.setLayout(layout)

    def handle_voltar(self):
        self.stacked_widget.setCurrentIndex(3)



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
        self.funcionarios = QPushButton("Funcionarios")
        self.discos = QPushButton("Discos")        
        self.emprestimo = QPushButton("Emprestimo")

        self.logout.clicked.connect(self.handle_logout)
        self.funcionarios.clicked.connect(self.handle_funcionarios)
        self.discos.clicked.connect(self.handle_discos)
        self.emprestimo.clicked.connect(self.handle_emprestimos)
        
        self.initUI()

    def initUI(self):
        layout = QGridLayout()
            
        layout.addWidget(self.logout, 0, 0)
        layout.addWidget(self.funcionarios, 1, 0)
        layout.addWidget(self.discos, 2, 0)
        layout.addWidget(self.emprestimo, 3, 0)
        
        layout.addWidget(self.funcionarios)

        self.setLayout(layout)

    def handle_logout(self):
        global usuario_atual
        usuario_atual = Usuario("", "", -1, "", "", "")
        self.stacked_widget.setCurrentIndex(0)

    def handle_funcionarios(self):
        global usuario_atual
        if usuario_atual.get_cargo() == "Funcionario":
            self.stacked_widget.setCurrentIndex(4)

    def handle_discos(self):
        self.stacked_widget.setCurrentIndex(5)

    def handle_emprestimos(self):
        self.stacked_widget.setCurrentIndex(6)

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
        self.discos = Discos(self.stacked_widget)
        self.emprestimos = Emprestimos(self.stacked_widget)
        
        self.stacked_widget.addWidget(self.menuWindow)
        self.stacked_widget.addWidget(self.loginWindow)
        self.stacked_widget.addWidget(self.registerWindow)
        self.stacked_widget.addWidget(self.menuLogin)
        self.stacked_widget.addWidget(self.funcionarios)
        self.stacked_widget.addWidget(self.discos)
        self.stacked_widget.addWidget(self.emprestimos)

        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stacked_widget)
        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
