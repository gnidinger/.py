from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2023, 11, 13),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "ec2_post_request_daily_KST",
    default_args=default_args,
    description="Send POST request to EC2 instance every midnight",
    schedule_interval="0 15 * * *",  # 매일 자정
    catchup=False,
)

post_request_task = SimpleHttpOperator(
    task_id="send_post_request",
    http_conn_id="copykle_http_connection",  # 설정한 HTTP 연결 ID
    endpoint="/api/auto-bot/batch",  # EC2 인스턴스의 엔드포인트
    method="POST",
    headers={"Content-Type": "application/json"},
    dag=dag,
)

post_request_task
