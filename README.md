# Projeto ETL Criptomoedas

Este projeto faz parte do meu Trabalho de Conclusão de Curso (TCC) e tem como objetivo construir uma **pipeline ETL completa** para extração, transformação e carregamento de dados de criptomoedas.

O projeto coleta dados das APIs públicas da [Coinbase](https://api.coinbase.com) e armazena os resultados em um banco de dados PostgreSQL, utilizando Apache Airflow para orquestração e Streamlit para visualização dos dados.

---

## 🔧 Tecnologias Utilizadas

- **Python 3.12**
- **Apache Airflow** (via Astro CLI)
- **Docker e Docker Compose**
- **PostgreSQL**
- **SQLAlchemy**
- **Pandas**
- **Requests**
- **Streamlit**
- **Coinbase API**

---

## 📊 Criptomoedas Monitoradas

- **Bitcoin (BTC)**
- **Ethereum (ETH)**  
*(Planejado: Solana)*

Cada criptomoeda possui:
- Uma tabela dedicada no PostgreSQL
- Uma DAG separada no Airflow
- Uma aba exclusiva no dashboard Streamlit

---

## 📁 Estrutura do Projeto

```text
projeto_cripto_etl/
├── dags/
│   ├── cripto_etl_dag.py              # DAG para Bitcoin
│   └── dag_ethereum.py                # DAG para Ethereum
├── include/
│   └── etl/
│       ├── extract.py                 # Extração de dados Bitcoin
│       ├── transform.py              # Transformação Bitcoin
│       ├── load.py                   # Carga de dados Bitcoin
│       ├── extract_ethereum.py       # Extração Ethereum
│       ├── transform_ethereum.py     # Transformação Ethereum
│       ├── load_ethereum.py          # Carga Ethereum
│       └── database/
│           ├── tabela_bitcoin_precos.py
│           └── tabela_ethereum_precos.py
├── streamlit_app/
│   ├── app.py                         # Dashboard Streamlit
│   ├── Dockerfile
│   └── requirements.txt
├── tests/                            
├── .env                               # Variáveis de ambiente
├── docker-compose.yml                 # Orquestra os containers
├── airflow_settings.yaml              # Conexão PostgreSQL no Airflow
├── Dockerfile                         # Dockerfile principal 
└── README.md                          # Este arquivo
```

1. Clone o repositório

git clone https://github.com/seu-usuario/projeto_cripto_etl.git
cd projeto_cripto_etl

2. Suba os containers

# Inicia o ambiente do Apache Airflow
astro dev start

# Em outro terminal, inicia o dashboard Streamlit
docker compose up streamlit

3. Acesse os serviços
🔁 Airflow: http://localhost:8080

📊 Streamlit Dashboard: http://localhost:8501

🗄️ PostgreSQL (via PgAdmin ou outro): localhost:5432

🛠️ Em Desenvolvimento
✅ Adição de novas criptomoedas (ex: Solana)

📈 Criação de dashboards adicionais (Power BI)

☁️ Deploy na nuvem via VPS

👨‍💻 Autor
Vitor Justiniano
Engenharia de Dados | Python | SQL | Airflow | PostgreSQL
https://www.linkedin.com/in/vitor-justiniano-b6425421a
