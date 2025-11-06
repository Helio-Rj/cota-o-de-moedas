"""
Aplicativo de Cotações com Interface Gráfica (comentado para aprendizado)

Este arquivo cria uma janela simples usando PyQt6 que consulta a API
da AwesomeAPI para obter as cotações do Dólar, Euro e Bitcoin em Reais
e exibe esses valores formatados na interface.

Comentários foram adicionados em cada seção para fins didáticos.
"""

import sys
import requests

# PyQt6: framework para criar interfaces gráficas (GUI)
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QLabel, QFrame
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont


class JanelaPrincipal(QMainWindow):
    """
    JanelaPrincipal é a classe que representa a janela principal do app.

    Ela herda QMainWindow, que é um tipo de janela com recursos
    prontos (barra de título, ícones, área central etc.).
    """

    def __init__(self):
        # Chama o construtor da classe pai
        super().__init__()

        # ---------- Configuração básica da janela ----------
        self.setWindowTitle("Cotações em Tempo Real")
        self.setMinimumSize(400, 300)  # Tamanho mínimo da janela

        # Estilo visual (CSS simples aplicado aos widgets)
        # Permite separar a lógica da aparência e deixa a UI mais agradável
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QLabel {
                color: #2c3e50;
                background-color: white;
                border-radius: 10px;
                padding: 15px;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QFrame {
                background-color: white;
                border-radius: 15px;
            }
        """)

        # ---------- Estrutura de widgets e layout ----------
        # widget_central é o widget que fica dentro da janela principal
        widget_central = QWidget()
        self.setCentralWidget(widget_central)

        # Layout vertical principal: organiza widgets um abaixo do outro
        layout = QVBoxLayout(widget_central)
        layout.setContentsMargins(20, 20, 20, 20)  # margens internas
        layout.setSpacing(15)  # espaço entre widgets

        # Frame (caixa) para conter as labels das cotações
        frame_cotacoes = QFrame()
        layout_cotacoes = QVBoxLayout(frame_cotacoes)
        layout_cotacoes.setContentsMargins(15, 15, 15, 15)
        layout_cotacoes.setSpacing(10)

        # Fontes usadas para título e valores
        fonte_titulo = QFont("Arial", 16, QFont.Weight.Bold)
        fonte_cotacao = QFont("Arial", 14)

        # Label de título (centralizado)
        self.label_titulo = QLabel("Cotações em Tempo Real")
        self.label_titulo.setFont(fonte_titulo)
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Labels que mostrarão as cotações (iniciam com texto de carregando)
        self.label_dolar = QLabel("Dólar: Carregando...")
        self.label_euro = QLabel("Euro: Carregando...")
        self.label_btc = QLabel("Bitcoin: Carregando...")

        # Aplica a mesma fonte e alinhamento para cada label de valor
        for label in [self.label_dolar, self.label_euro, self.label_btc]:
            label.setFont(fonte_cotacao)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Botão que permite ao usuário forçar uma atualização imediata
        self.botao_atualizar = QPushButton("Atualizar Cotações")
        # Conecta o evento de clique do botão ao método atualizar_cotacoes
        self.botao_atualizar.clicked.connect(self.atualizar_cotacoes)

        # Adiciona widgets ao layout do frame e ao layout principal
        layout_cotacoes.addWidget(self.label_titulo)
        layout_cotacoes.addWidget(self.label_dolar)
        layout_cotacoes.addWidget(self.label_euro)
        layout_cotacoes.addWidget(self.label_btc)

        layout.addWidget(frame_cotacoes)
        layout.addWidget(self.botao_atualizar)

        # ---------- Timer para atualização automática ----------
        # QTimer dispara um sinal (timeout) periodicamente
        self.timer = QTimer()
        self.timer.timeout.connect(self.atualizar_cotacoes)
        self.timer.start(60000)  # atualiza a cada 60.000 ms = 60 segundos

        # Faz a primeira atualização imediatamente ao abrir a janela
        self.atualizar_cotacoes()

    def atualizar_cotacoes(self):
        """
        Método que consulta a API de cotações e atualiza os labels da UI.

        Passos:
        1. Faz uma requisição HTTP para a API (requests.get)
        2. Converte a resposta JSON para dicionário (resposta.json())
        3. Extrai os valores (bid) e converte para float
        4. Formata os valores e atualiza os widgets na interface
        5. Em caso de erro, exibe mensagens amigáveis na UI
        """
        try:
            # Faz a requisição para a API que retorna vários pares em JSON
            requisicao = requests.get(
                "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"
            )

            # .json() converte o texto JSON para um dict Python
            requisicao_dic = requisicao.json()

            # Extrai o preço de venda (bid) de cada par e converte para float
            cotacao_dolar = float(requisicao_dic['USDBRL']['bid'])
            cotacao_euro = float(requisicao_dic['EURBRL']['bid'])
            cotacao_btc = float(requisicao_dic['BTCBRL']['bid'])

            # Formata os números para exibir com separador de milhares
            # e duas casas decimais: {valor:,.2f}
            self.label_dolar.setText(f"Dólar: R$ {cotacao_dolar:,.2f}")
            self.label_euro.setText(f"Euro: R$ {cotacao_euro:,.2f}")
            self.label_btc.setText(f"Bitcoin: R$ {cotacao_btc:,.2f}")

            # Feedback visual para o usuário: botão indica atualização
            self.botao_atualizar.setText("Cotações Atualizadas!")
            # Volta o texto do botão ao normal após 2 segundos
            QTimer.singleShot(2000, lambda: self.botao_atualizar.setText("Atualizar Cotações"))

        except Exception as e:
            # Tratamento simples de erros: exibe mensagens nas labels
            # Em aplicações maiores você pode mostrar um modal ou log.
            self.label_dolar.setText("Erro ao atualizar cotações")
            self.label_euro.setText("Verifique sua conexão")
            # Converte o erro em string para ajudar no diagnóstico
            self.label_btc.setText(f"Erro: {str(e)}")


if __name__ == '__main__':
    # Ponto de entrada: cria a aplicação Qt e abre a janela
    # QApplication gerencia o loop de eventos e configurações da app
    app = QApplication(sys.argv)

    # Cria a janela principal e exibe na tela
    janela = JanelaPrincipal()
    janela.show()

    # Inicia o loop de eventos (necessário para a interface responder a eventos)
    sys.exit(app.exec())
