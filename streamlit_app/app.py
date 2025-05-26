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
query = "SELECT * FROM bitcoin_precos ORDER BY timestamp DESC LIMIT 1000"
df = pd.read_sql(query, engine)

# Pré-processamento
df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df.sort_values("timestamp")

# Layout
st.set_page_config(page_title="Bitcoin Dashboard", layout="wide")
st.title("📈 Dashboard de Preços do Bitcoin")

# Filtro por data
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Data inicial", df['timestamp'].min().date())
with col2:
    end_date = st.date_input("Data final", df['timestamp'].max().date())

filtered_df = df[(df['timestamp'].dt.date >= start_date) & (df['timestamp'].dt.date <= end_date)]

# KPIs
latest_price = filtered_df.iloc[-1]['valor']
max_price = filtered_df['valor'].max()
min_price = filtered_df['valor'].min()
avg_price = filtered_df['valor'].mean()

kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("💰 Último Preço", f"R$ {latest_price:,.2f}")
kpi2.metric("📈 Máximo", f"R$ {max_price:,.2f}")
kpi3.metric("📉 Mínimo", f"R$ {min_price:,.2f}")
kpi4.metric("📊 Média", f"R$ {avg_price:,.2f}")

# Gráfico de linha
st.subheader("📊 Evolução do Preço")
st.line_chart(filtered_df.set_index('timestamp')['valor'])

# Tabela de dados
st.subheader("🔍 Dados Recentes")
st.dataframe(filtered_df.tail(20), use_container_width=True)