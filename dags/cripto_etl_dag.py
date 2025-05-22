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
    description='Pipeline ETL para dados de criptomoedas com Airflow',
    schedule_interval='0 */8 * * *',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['cripto', 'etl']
) as dag:

    def tarefa_extract_func(ti):
        criar_tabela()  # garante que a tabela existe
        dados = extrair_dados_bitcoin()
        if not dados:
            raise ValueError("Erro ao extrair os dados")
        ti.xcom_push(key='dados_json', value=dados)

    def tarefa_transform_func(ti):
        dados_json = ti.xcom_pull(key='dados_json', task_ids='extrair_dados')
        if not dados_json:
            raise ValueError("Nenhum dado para transformar")
        dados_tratados = tratar_dados_bitcoin(dados_json)
        ti.xcom_push(key='dados_tratados', value=dados_tratados)

    def tarefa_load_func(ti):
        dados_tratados = ti.xcom_pull(key='dados_tratados', task_ids='transformar_dados')
        if not dados_tratados:
            raise ValueError("Nenhum dado para carregar")
        salvar_dados_postgres(dados_tratados)

    tarefa_extract = PythonOperator(
        task_id='extrair_dados',
        python_callable=tarefa_extract_func
    )

    tarefa_transform = PythonOperator(
        task_id='transformar_dados',
        python_callable=tarefa_transform_func
    )

    tarefa_load = PythonOperator(
        task_id='carregar_dados',
        python_callable=tarefa_load_func
    )

    tarefa_extract >> tarefa_transform >> tarefa_load
