import pandas as pd
import json
from datetime import datetime

def tratar_dados_ethereum():
    with open('/tmp/dados_eth.json', 'r') as f:
        dados_json = json.load(f)

    valor = float(dados_json['data']['amount'])
    criptomoeda = dados_json['data']['base']
    moeda = dados_json['data']['currency']
    timestamp = datetime.now().isoformat()

    df = pd.DataFrame([{
        "valor": valor,
        "criptomoeda": criptomoeda.upper(),
        "moeda": moeda.upper(),
        "timestamp": timestamp
    }])

    df = df.dropna()
    dados_tratados = df.iloc[0].to_dict()

    with open('/tmp/dados_tratados_eth.json', 'w') as f:
        json.dump(dados_tratados, f)
