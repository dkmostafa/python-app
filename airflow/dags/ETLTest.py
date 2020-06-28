from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'Mostafa Dekmak',
    'depends_on_past': False,
    'start_date': datetime(2016, 4, 15),
    # 'schedule_interval': '@hourly',
    'email': ['dekmakmostafa@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 4,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG('etl_task', default_args=default_args, schedule_interval='*/10 * * * *')


def run_etl(ds, **kwargs):
    # print(pd.__version);
    # get the version of the pandas for testing
    print('Ad Stat ETL Starts');



run_this = PythonOperator(
    task_id='run_etl',
    provide_context=True,
    python_callable=run_etl,
    dag=dag)
