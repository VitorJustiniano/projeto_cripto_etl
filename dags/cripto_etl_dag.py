from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from include.etl.extract import extrair_dados_bitcoin
from include.etl.transform import tratar_dados_bitcoin
from include.etl.load import salvar_dados_postgres
from include.etl.database.tabela_bitcoin_precos import criar_tabela

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='cripto_etl_dag',
    default_args=default_args,
    description='Pipeline ETL com arquivos temporários JSON',
    schedule_interval='0 */8 * * *',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['cripto', 'etl']
) as dag:

    extrair = PythonOperator(
        task_id='extrair_dados',
        python_callable=extrair_dados_bitcoin
    )

    transformar = PythonOperator(
        task_id='transformar_dados',
        python_callable=tratar_dados_bitcoin
    )

    carregar = PythonOperator(
        task_id='carregar_dados',
        python_callable=salvar_dados_postgres
    )

    extrair >> transformar >> carregar