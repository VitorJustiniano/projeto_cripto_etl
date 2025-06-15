import requests
import json

def extrair_dados_ethereum():
    url = 'https://api.coinbase.com/v2/prices/ETH-USD/spot'
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        with open('/tmp/dados_eth.json', 'w') as f:
            json.dump(dados, f)
    else:
        raise ValueError(f"Erro na API: {resposta.status_code}")