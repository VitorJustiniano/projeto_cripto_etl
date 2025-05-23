import requests
import json

def extrair_dados_bitcoin():
    """Extrai o JSON completo da API da Coinbase e salva localmente."""
    url = 'https://api.coinbase.com/v2/prices/spot'
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        with open('/tmp/dados_extraidos.json', 'w') as f:
            json.dump(dados, f)
    else:
        print(f"Erro na API: {resposta.status_code}")
        raise ValueError("Falha ao extrair os dados")