from airflow import DAG, Dataset
from airflow.decorators import task
from datetime import datetime

#DEFINING DATASET
my_file = Dataset('/tmp/my_file.txt') # DATASET(<URI>,<EXTRA>)
my_file_2 = Dataset('/tmp/my_file_2.txt')

# DEFINING DAG
with DAG (
    dag_id = 'consumer_dag',
    start_date = datetime(2023,6,14),
    schedule = [my_file,my_file_2],
    catchup = False
) as dag :
    
    @task
    def read_dataset():
        with open(my_file.uri, 'r') as f:
            print(f.read())
            
    read_dataset()
