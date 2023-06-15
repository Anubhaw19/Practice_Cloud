from airflow import DAG, Dataset
from datetime import datetime
from airflow.decorators import task # easy way of defining tasks (Python Operator)

#DEFINING DATASET
my_file = Dataset('/tmp/my_file.txt') # DATASET(<URI>,<EXTRA>)
my_file_2 = Dataset('/tmp/my_file_2.txt')

with DAG(
    dag_id = 'producer_dag',
    start_date = datetime(2023,6,15) ,
    schedule = '@daily',
    catchup = False
    ) as dag :
    
    @task(outlets=[my_file])
    def update_dataset():
        with open(my_file.uri, 'a+') as f:
            f.write("producer updated\n")
    
    @task(outlets=[my_file_2])
    def update_dataset_2():
        with open(my_file_2.uri,'a+') as f:
            f.write("producer 2 updated\n")
    
    update_dataset() >> update_dataset_2()

            
    
            
            
        
