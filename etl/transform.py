import pandas as pd
from datetime import datetime

def tratar_dados_bitcoin(dados_json):
    """Transforma os dados brutos da API, converte em Dataframe e aplica os tratamentos."""
    
    valor = float(dados_json['data']['amount'])
    criptomoeda = dados_json['data']['base']
    moeda = dados_json['data']['currency']
    timestamp = datetime.now()
    

    df = pd.DataFrame([{
        "valor": valor,
        "criptomoeda": criptomoeda,
        "moeda": moeda,
        "timestamp": timestamp
    }])

    #Garantir que os tipos estao corretos
    df['valor'] = pd.to_numeric(df['valor'], errors='coerce')
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    #Normalizar texto
    df['criptomoeda'] = df['criptomoeda'].str.upper()
    df['moeda'] = df['moeda'].str.upper()

    #Remove valores nulos
    df = df.dropna()

    return df.iloc[0].to_dict()