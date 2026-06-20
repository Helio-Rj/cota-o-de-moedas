import exec_api
import requests


class DummyResponse:
    def __init__(self, data, status=200):
        self._data = data
        self.status_code = status

    def json(self):
        return self._data

    def raise_for_status(self):
        if self.status_code != 200:
            raise requests.HTTPError(f"status {self.status_code}")


def test_execucao(monkeypatch, capsys):
    """Mocka a chamada externa para economia.awesomeapi.com.br para tornar o teste determinístico."""
    fake = {
        "USDBRL": {"bid": "5.00"},
        "EURBRL": {"bid": "5.50"},
        "BTCBRL": {"bid": "120000.0"},
    }

    # Substitui exec_api.requests.get por uma função que retorna DummyResponse
    monkeypatch.setattr(exec_api.requests, "get", lambda url: DummyResponse(fake))

    # Executa a função — agora sem depender da API externa
    exec_api.pegar_cotacoes()

    # Captura a saída e verifica conteúdo mínimo
    captured = capsys.readouterr()
    assert "Cotações Atuais" in captured.out
    assert "Dólar" in captured.out
    assert "Euro" in captured.out
    assert "Bitcoin" in captured.out
