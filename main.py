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

O Cx_freeze é um módulo que permite gerar um arquivo executável do python.
Para gerar o arquivo executável, é preciso criar um arquivo setup.py com as configurações do programa.
Após gerar o arquivo setup.py, é preciso executar o comando:
    python setup.py build
"""
from web_scraping import gerar_pessoa
from display import *
from PyQt5.QtWidgets import QMainWindow, QApplication


class Pessoa(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        # Carregando os dados na inicialização da janela
        self.carregar_dados()
        
        # Recarregando os dados ao clicar no botão
        self.btnGerarPessoa.clicked.connect(self.carregar_dados)


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
