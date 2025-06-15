from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from include.etl.database.tabela_ethereum_precos import criar_tabela
from include.etl.extract_ethereum import extrair_dados_ethereum
from include.etl.transform_ethereum import tratar_dados_ethereum
from include.etl.load_ethereum import salvar_dados_postgres_ethereum

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='cripto_etl_ethereum_dag',
    default_args=default_args,
    description='Pipeline ETL Ethereum com criação da tabela',
    schedule_interval='0 */8 * * *',  # roda a cada 8 horas
    start_date=datetime(2025, 6, 15),
    catchup=False,
    tags=['cripto', 'ethereum', 'etl'],
) as dag:

    extrair = PythonOperator(
        task_id='extrair_dados_ethereum',
        python_callable=extrair_dados_ethereum,
    )

    transformar = PythonOperator(
        task_id='tratar_dados_ethereum',
        python_callable=tratar_dados_ethereum,
    )

    carregar = PythonOperator(
        task_id='carregar_dados_ethereum',
        python_callable=salvar_dados_postgres_ethereum,
    )

    # Definindo ordem das tasks
    extrair >> transformar >> carregar
