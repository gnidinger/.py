from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# DAG 이름과 스케줄링 주기를 정의합니다.
dag = DAG(
    "simple_dag",
    start_date=datetime(2023, 10, 4),  # DAG가 시작하는 날짜를 설정합니다.
    schedule_interval=None,  # DAG의 실행 빈도를 설정합니다. 여기서는 수동으로 실행하기 위해 None으로 설정합니다.
    catchup=False,  # 과거 작업을 실행하지 않도록 설정합니다.
    tags=["example"],  # DAG에 태그를 추가합니다.
)

# BashOperator를 사용하여 "Hello, Airflow!"를 출력하는 작업을 정의합니다.
hello_task = BashOperator(
    task_id="hello_task",
    bash_command='echo "Hello, Airflow World!"',
    dag=dag,
)

# 작업 간의 의존성을 설정합니다.
hello_task
