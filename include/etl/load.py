import json
from datetime import datetime
from include.etl.database.tabela_bitcoin_precos import get_session, BitcoinPreco

def salvar_dados_postgres():
    """Lê o JSON tratado e insere no banco PostgreSQL."""
    with open('/tmp/dados_tratados.json', 'r') as f:
        dados = json.load(f)

    dados['timestamp'] = datetime.fromisoformat(dados['timestamp'])

    session = get_session()
    novo_registro = BitcoinPreco(**dados)
    session.add(novo_registro)
    session.commit()
    session.close()
    print(f"[{dados['timestamp']}] Dados salvos no PostgreSQL!")