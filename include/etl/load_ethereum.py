import json
from datetime import datetime
from include.etl.database.tabela_ethereum_precos import get_session, EthereumPreco

def salvar_dados_postgres_ethereum():
    with open('/tmp/dados_tratados_eth.json', 'r') as f:
        dados = json.load(f)

    dados['timestamp'] = datetime.fromisoformat(dados['timestamp'])

    session = get_session()
    novo_registro = EthereumPreco(**dados)
    session.add(novo_registro)
    session.commit()
    session.close()
    print(f"[{dados['timestamp']}] Dados Ethereum salvos no PostgreSQL!")