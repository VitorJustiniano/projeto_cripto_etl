import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente
load_dotenv()
engine = create_engine(os.getenv("DB_CONN"))

st.set_page_config(page_title="Dashboard Cripto", layout="wide")
st.title("📊 Dashboard de Criptomoedas")

# Função genérica para carregar e exibir os dados
def exibir_dashboard(tabela, nome_exibicao):
    # Consulta SQL
    query = f"SELECT * FROM {tabela} ORDER BY timestamp DESC LIMIT 1000"
    df = pd.read_sql(query, engine)

    # Pré-processamento
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values("timestamp")

    # Filtro por data
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input(f"{nome_exibicao} - Data inicial", df['timestamp'].min().date(), key=f"{tabela}_start")
    with col2:
        end_date = st.date_input(f"{nome_exibicao} - Data final", df['timestamp'].max().date(), key=f"{tabela}_end")

    filtered_df = df[(df['timestamp'].dt.date >= start_date) & (df['timestamp'].dt.date <= end_date)]

    # KPIs
    if not filtered_df.empty:
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
        st.subheader(f"📊 Evolução do Preço - {nome_exibicao}")
        st.line_chart(filtered_df.set_index('timestamp')['valor'])

        # Tabela
        st.subheader("🔍 Dados Recentes")
        st.dataframe(filtered_df.tail(20), use_container_width=True)
    else:
        st.warning("⚠️ Nenhum dado encontrado para o período selecionado.")

# Abas
abas = st.tabs(["Bitcoin", "Ethereum"])

with abas[0]:
    exibir_dashboard("bitcoin_precos", "Bitcoin (BTC)")

with abas[1]:
    exibir_dashboard("ethereum_precos", "Ethereum (ETH)")