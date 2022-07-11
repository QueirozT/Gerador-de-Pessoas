"""
Este programa gera dados falsos de uma pessoa

Os dados falsos são gerados aleatoriamente e coletados de uma página web.
O módulo web_scraping responsável por fazer a requisição e coletar os dados, fornecendo através de um dicionário.

Comandos Utilizados:
    Instalação: 
        pip install requests
        pip install beautifulsoup4
        pip install pyqt5
        pip install cx_freeze

    Conversão de arquivo .ui:
        pyuic5 GUI.ui -o display.py

Usando o CX_Freeze:
    O Cx_freeze é um módulo que permite gerar um arquivo executável do python.
    Para gerar o arquivo executável, é preciso criar um arquivo setup.py com as configurações do programa.
    Após gerar o arquivo setup.py, é preciso executar o comando:
        python setup.py build

Usando o Pyinstaller:
    O Pyinstaller é um módulo que permite gerar um arquivo executável do python.
    Para gerar o arquivo executável, basta executar o comando:
        pyinstaller --noconsole --name="Gerador_de_Pessoas" --icon="icon.ico" --onefile main.py
"""
from web_scraping import gerar_pessoa
from display import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5.QtCore import Qt, QTimer


class Pessoa(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        # Carregando os dados na inicialização da janela
        self.carregar_dados()

        # Definindo um timer para resetar modificações
        self.timer = QTimer(self)
        self.lista_widgets = list()
        self.timer.timeout.connect(self.resetar)

        # Criando filtro de eventos para os campos de texto.
        self._Nome.installEventFilter(self)
        self._CPF.installEventFilter(self)
        self._Idade.installEventFilter(self)
        self._Nascimento.installEventFilter(self)
        self._Email.installEventFilter(self)
        self._Telefone.installEventFilter(self)
        self._Endereco.installEventFilter(self)
        self._Cidade.installEventFilter(self)
        self._Estado.installEventFilter(self)
        self._Cep.installEventFilter(self)
        self._Altura.installEventFilter(self)
        self._Peso.installEventFilter(self)
        self._Sangue.installEventFilter(self)
        
        # Recarregando os dados ao clicar no botão
        self.btnGerarPessoa.clicked.connect(self.carregar_dados)


    def eventFilter(self, obj, event):
        """
        Este Método sobrescreve o Filtro de eventos da classe QWidget
        Isso permite que o evento de clique seja capturado junto com o objeto que está sendo filtrado.

        :param obj: Objeto que está sendo filtrado
        :param event: Evento que está sendo filtrado
        :return: Os mesmos valores do filtro para o método original do eventFilter
        """
        if event.type() == event.MouseButtonPress:  # Validando o tipo de evento
            obj.setCursor(Qt.ClosedHandCursor)
            obj.selectAll()
            obj.copy()
            obj.setStyleSheet("background-color: green;color: white;border-radius: 10px;border: 2px solid grey;")
            self.lista_widgets.append(obj)  # Adicionando o objeto a lista de widgets
            self.timer.start(300)  # Iniciando o timer
        return super(QWidget, self).eventFilter(obj, event)  # Repassando o Filtro de Evento para a classe original


    def resetar(self):
        for item in self.lista_widgets:
            item.setCursor(Qt.IBeamCursor)
            item.setStyleSheet("background-color: white;color: black;border-radius: 10px;border: 2px solid grey;")
        self.lista_widgets.clear()
        self.timer.stop()


    def carregar_dados(self):
        pessoa = gerar_pessoa()
        if pessoa:
            self._Nome.setText(pessoa['nome'])
            self._CPF.setText(pessoa['cpf'])
            self._Idade.setText(pessoa['idade'])
            self._Nascimento.setText(pessoa['data_nascimento'])
            self._Email.setText(pessoa['email'])
            self._Telefone.setText(pessoa['telefone'])
            self._Endereco.setText(pessoa['endereco'])
            self._Cidade.setText(pessoa['cidade'])
            self._Estado.setText(pessoa['estado'])
            self._Cep.setText(pessoa['cep'])
            self._Altura.setText(pessoa['altura'])
            self._Peso.setText(pessoa['peso'])
            self._Sangue.setText(pessoa['tipo_sanguineo'])


if __name__ == "__main__":
    app = QApplication([])

    window = Pessoa()

    window.show()
    app.exec_()
