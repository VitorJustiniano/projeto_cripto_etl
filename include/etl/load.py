from include.etl.database.tabela_bitcoin_precos import get_session, BitcoinPreco

def salvar_dados_postgres(dados):
    session = get_session()
    novo_registro = BitcoinPreco(**dados)
    session.add(novo_registro)
    session.commit()
    session.close()
    print(f"[{dados['timestamp']}] Dados salvos no PostgreSQL!")