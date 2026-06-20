
# Cotação de Moedas 💱

Para este aplicativo em Python para consultar cotações em tempo real de Dólar, Euro e ‘Bitcoin’ em Reais (BRL), utilizando a API da AwesomeAPI. Possui ‘interface’ gráfica moderna com PyQt6 e versão de linha de comando.

## Funcionalidades
- Consulta automática e manual das cotações USD/BRL, EUR/BRL e BTC/BRL
- Interface gráfica intuitiva (PyQt6)
- Exibição dos valores formatados
- Atualização automática a cada minuto
- Versão CLI para uso rápido no terminal

## Captura de Tela
<img src="https://user-images.githubusercontent.com/placeholder/cotacoes_gui.png" alt="Exemplo da interface" width="400"/>

## Requisitos
- Python 3.8 ou superior
- [PyQt6](https://pypi.org/project/PyQt6/)
- [requests](https://pypi.org/project/requests/)

## Instalação
1. Clone o repositório:
	```bash
	git clone https://github.com/seu-usuario/cota-o-de-moedas.git
	cd cota-o-de-moedas
	```
2. Instale as dependências:
	```bash
	pip install -r requirements.txt
	```
	Ou manualmente:
	```bash
	pip install PyQt6 requests
	```

## Como Usar

### Interface Gráfica (GUI)
```bash
python cotacoes_gui.py
```

### Linha de Comando (CLI)
```bash
python exec_api.py
```

## Estrutura do Projeto
- `cotacoes_gui.py` — Aplicativo com interface gráfica
- `exec_api.py` — Consulta rápida via terminal
- `README.md` — Documentação
- `LICENSE` — Licença de uso

## Exemplo de Saída (CLI)
```
Cotações Atuais:
═══════════════════════
Dólar:   R$ 5,25
Euro:    R$ 5,70
Bitcoin: R$ 210.000,00
═══════════════════════
```

## Créditos
Desenvolvido por [Hélio do Nascimento](https://github.com/Helio-Rj)
API utilizada: [AwesomeAPI - Economia](https://docs.awesomeapi.com.br/api-de-moedas)

## Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
