import os
import time
import requests
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Importar Base e BitcoinPreco do database.py
from database.tabela_bitcoin_precos import Base, BitcoinPreco

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Lê as variáveis separadas do arquivo .env (sem SSL)
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

# Cria o engine e a sessão
DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def testar_conexao():
    try:
        engine = create_engine(DATABASE_URL)
        # Abre uma conexão e fecha imediatamente
        with engine.connect() as conexao:
            print(" Conexão com o banco de dados bem-sucedida!")
    except Exception as e:
        print(" Erro ao conectar com o banco de dados:")
        print(e)

if __name__ == "__main__":
    testar_conexao()
