from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime, timedelta

# Funktion für die Python-Task
def hello_world():
    print("Hello, Airflow!")

# Standard-DAG-Argumente
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# DAG-Definition
with DAG(
    'test_dag',
    default_args=default_args,
    description='Ein einfacher Test-DAG',
    schedule_interval=timedelta(days=1),  # Täglich ausführen
    start_date=datetime(2024, 11, 11),  # Startdatum für den DAG
    catchup=False,  # Verhindert, dass der DAG alte Ausführungen nachholt
) as dag:
    
    # Dummy-Operator, um einen Platzhalter zu erstellen
    start_task = DummyOperator(
        task_id='start_task',
    )
    
    # Python-Operator, der die Funktion `hello_world` ausführt
    hello_task = PythonOperator(
        task_id='hello_task',
        python_callable=hello_world,
    )
    
    # Dummy-Operator für das Ende der DAG
    end_task = DummyOperator(
        task_id='end_task',
    )
    
    # Task-Abhängigkeiten festlegen
    start_task >> hello_task >> end_task
