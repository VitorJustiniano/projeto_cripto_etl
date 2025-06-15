from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Float, String, Integer, DateTime, create_engine
from datetime import datetime
from airflow.hooks.base import BaseHook

Base = declarative_base()

class EthereumPreco(Base):
    __tablename__ = "ethereum_precos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Float, nullable=False)
    criptomoeda = Column(String(50), nullable=False)
    moeda = Column(String(10), nullable=False)
    timestamp = Column(DateTime, default=datetime.now)

def get_engine():
    conn = BaseHook.get_connection("pg_banco_externo")
    conn_str = f"postgresql://{conn.login}:{conn.password}@{conn.host}:{conn.port}/{conn.schema}"
    return create_engine(conn_str)

def get_session():
    engine = get_engine()
    return sessionmaker(bind=engine)()

def criar_tabela():
    engine = get_engine()
    Base.metadata.create_all(engine)