import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente
load_dotenv()

# Cria engine de conexão
engine = create_engine(os.getenv("DB_CONN"))

# Consulta SQL
query = "SELECT * FROM bitcoin_precos ORDER BY timestamp DESC LIMIT 100"

# Lê os dados
try:
    df = pd.read_sql(query, engine)

    # Interface do Streamlit
    st.set_page_config(page_title="Bitcoin Dashboard", layout="wide")
    st.title("💹 Dashboard de Preços do Bitcoin")

    st.subheader("Gráfico de Preços (Últimos Registros)")
    st.line_chart(df.sort_values("timestamp")["valor"])

    st.subheader("Tabela de Dados")
    st.dataframe(df)

except Exception as e:
    st.error("Erro ao conectar no banco de dados:")
    st.error(str(e))
