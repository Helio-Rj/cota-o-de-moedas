# ==================================================================
# PROGRAMA: Consulta de Cotações de Moedas
# OBJETIVO: Buscar cotações atuais do Dólar, Euro e Bitcoin em Reais
# ==================================================================

# Importa a biblioteca requests para fazer requisições HTTP
# Esta biblioteca permite que façamos chamadas a APIs ‘web’
import requests


def pegar_cotacoes():
    """
    Função que busca e exibe as cotações atuais de Dólar, Euro e ‘Bitcoin’.
    
    Utiliza a API da AwesomeAPI (economia.awesomeapi.com.br) para obter
    as cotações em tempo real.
    """
    # Faz uma requisição GET para a API
    # - USD-BRL: Dólar para Real
    # - EUR-BRL: Euro para Real
    # - BTC-BRL: ‘Bitcoin’ para Real
    requisicao = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")

    # Converte a resposta JSON para um dicionário Python
    # .json() é um método que transforma o texto JSON em estrutura de dados Python
    requisicao_dic = requisicao.json()

    # Extrai os valores de cotação do dicionário
    # - ['USDBRL'] acessa o par Dólar-Real
    # - ['bid'] pega o valor de venda atual
    # - float() converte a string para número decimal
    cotacao_dolar = float(requisicao_dic['USDBRL']['bid'])
    cotacao_euro = float(requisicao_dic['EURBRL']['bid'])
    cotacao_btc = float(requisicao_dic['BTCBRL']['bid'])

    # Cria uma string formatada com as cotações
    # Usa f-string (string literal formatada) do Python
    # - f""" ... """: permite string multi-linha
    # - {variavel:, .2f}: formata número com:
    #   , = separador de milhares
    #   .2 = duas casas decimais
    #   f = número float
    texto = f"""
    Cotações Atuais:
    ═══════════════════════
    Dólar:   R$ {cotacao_dolar:,.2f}
    Euro:    R$ {cotacao_euro:,.2f}
    Bitcoin: R$ {cotacao_btc:,.2f}
    ═══════════════════════
    """
    # Exibe o texto formatado
    print(texto)


# Executa a função quando o programa é rodado
# Este é o ponto de entrada do programa
pegar_cotacoes()

# ==================================================================
# NOTAS DE APRENDIZADO:
# 1. APIs ‘Web’: usamos 'requests' para comunicação com serviços ‘web’
# 2. JSON: Formato padrão para dados na ‘web’, convertido para dict
# 3. F-strings: formatação moderna de ‘strings’ no Python (Python 3.6+)
# 4. Formatação numérica: Uso de:, .2f para formatar números
# 5. Docstrings: Documentação de funções com """… """
# ==================================================================
