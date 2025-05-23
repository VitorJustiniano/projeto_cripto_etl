import pandas as pd
import json
from datetime import datetime

def tratar_dados_bitcoin():
    """Transforma os dados extraídos e salva em JSON tratado."""
    with open('/tmp/dados_extraidos.json', 'r') as f:
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

    with open('/tmp/dados_tratados.json', 'w') as f:
        json.dump(dados_tratados, f)