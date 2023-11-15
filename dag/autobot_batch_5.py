from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator  # 수정됨
from datetime import datetime, timedelta
import pendulum

# 한국 시간대로 설정
local_tz = pendulum.timezone("Asia/Seoul")

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": pendulum.datetime(2023, 11, 13, tz="Asia/Seoul"),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "ec2_post_request_hourly_KST",
    default_args=default_args,
    description="Send POST request to EC2 instance every hour KST",
    schedule_interval="@hourly",  # 매 시간 실행
    catchup=False,
)

post_request_task = SimpleHttpOperator(
    task_id="send_post_request",
    http_conn_id="copykle_http_connection",
    endpoint="/api/auto-bot/batch",
    method="POST",
    headers={"Content-Type": "application/json"},
    dag=dag,
)

post_request_task
