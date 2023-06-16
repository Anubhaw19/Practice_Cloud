from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.subdag import SubDagOperator
from sub_dags.subdag_download import subdag_download # subdag_download is a function defined in subdag_download.py file
from datetime import datetime
from sub_dags.subdag_transform import subdag_transform # subdag_transform is a function defined in subdag_transform.py file

 
 
with DAG('sub_group_dag', start_date=datetime(2022, 1, 1), 
    schedule_interval='@daily', catchup=False) as dag:
    
    args = {'start_date': dag.start_date ,'schedule_interval': dag.schedule_interval, 'catchup' : dag.catchup }
    
    download = SubDagOperator(
        task_id = 'download',
        subdag =  subdag_download(dag.dag_id,'download',args)
    )
 
    # download_a = BashOperator(
    #     task_id='download_a',
    #     bash_command='sleep 10'
    # )
 
    # download_b = BashOperator(
    #     task_id='download_b',
    #     bash_command='sleep 10'
    # )
 
    # download_c = BashOperator(
    #     task_id='download_c',
    #     bash_command='sleep 10'
    # )
 
    check_files = BashOperator(
        task_id='check_files',
        bash_command='sleep 10'
    )
    
    transform = SubDagOperator(
        task_id = 'transform',
        subdag = subdag_transform(dag.dag_id, 'transform', args)
    )
 
    # transform_a = BashOperator(
    #     task_id='transform_a',
    #     bash_command='sleep 10'
    # )
 
    # transform_b = BashOperator(
    #     task_id='transform_b',
    #     bash_command='sleep 10'
    # )
 
    # transform_c = BashOperator(
    #     task_id='transform_c',
    #     bash_command='sleep 10'
    # )
 
    # [download_a, download_b, download_c] >> check_files >> [transform_a, transform_b, transform_c]
    download >> check_files >> transform