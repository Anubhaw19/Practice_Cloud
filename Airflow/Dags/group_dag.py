from airflow import DAG
from airflow.operators.bash import BashOperator
from groups.group_downloads import download_task
from groups.group_transform import transform_task
from datetime import datetime
  
with DAG('group_dag', start_date=datetime(2022, 1, 1), 
    schedule_interval='@daily', catchup=False) as dag:
    
    download = download_task()
 
    check_files = BashOperator(
        task_id='check_files',
        bash_command='sleep 10'
    )
    
    transform = transform_task()
 

    download >> check_files >> transform