from airflow import DAG
from airflow.providers.http.operators.http import HttpOperator
from datetime import datetime, timedelta
import pendulum

# 한국 시간대 설정
local_tz = pendulum.timezone("Asia/Seoul")

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    # 한국 시간대로 설정된 시작 날짜
    "start_date": pendulum.datetime(2023, 11, 13, tz="Asia/Seoul"),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "ec2_post_request_daily",
    default_args=default_args,
    description="Send POST request to EC2 instance every midnight KST",
    # UTC 기준으로 15:00 (KST 기준으로 다음날 자정)
    schedule_interval="0 15 * * *",
    catchup=False,
)

post_request_task = HttpOperator(
    task_id="send_post_request",
    http_conn_id="copykle_http_connection",
    endpoint="/api/auto-bot/batch",
    method="POST",
    headers={"Content-Type": "application/json"},
    dag=dag,
)

post_request_task
