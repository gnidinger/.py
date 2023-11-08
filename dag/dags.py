import json
import os
from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.python_operator import BranchPythonOperator


def print_hello():
    return "Hello world!"


def sms(**context):
    # current_dir = os.getcwd()
    context["task_instance"].xcom_push(key="pushed_value", value="xcom_push")
    # return current_dir


def pull_data(**context):
    # task_instance = {'1':'sms','2':'seoul','3':[{'a':'man','b':'happy'}]}
    # aa = task_instance.xcom_pull('copy', key='1')
    aa = context["task_instance"].xcom_pull(task_ids="hello_task", key="pushed_value")
    print("this is " + aa)
    context["task_instance"].xcom_push(key="xcom", value=aa)
    # return aa


options = ["xcom_push", "b_data"]


def fall_test(**context):
    if (
        context["task_instance"].xcom_pull(task_ids="copy_xcom", key="xcom")
        == "xcom_push"
    ):
        task_id = "xcom_push"
    else:
        task_id = "b_data"
    context["task_instance"].xcom_push(key="fall_test", value="22222")
    return task_id


def xcom_push(**context):
    context["task_instance"].xcom_push(key="fall_value", value="1")


def b_data(**context):
    context["task_instance"].xcom_push(key="fall_value", value="10000")


def last_function(**context):
    # for op in options:
    if (
        context["task_instance"].xcom_pull(task_ids="fall_test", key="fall_test")
        == "22222"
    ):
        last = context["task_instance"].xcom_pull(
            task_ids="xcom_push", key="fall_value"
        )
    else:
        last = context["task_instance"].xcom_pull(task_ids="b_data", key="fall_value")
    context["task_instance"].xcom_push(key="last_value", value=last)


dag = DAG(
    "hello_world",
    description="Simple tutorial DAG",
    # schedule_interval='*/1 * * * *',
    default_args={"provide_context": True},
    start_date=datetime(2023, 11, 7),
    catchup=False,
)

dummy_operator = DummyOperator(task_id="dummy_task", retries=3, dag=dag)

hello_operator = PythonOperator(task_id="hello_task", python_callable=sms, dag=dag)

copy_operator = PythonOperator(task_id="copy_xcom", python_callable=pull_data, dag=dag)

branch_operator = BranchPythonOperator(
    task_id="fall_test", python_callable=fall_test, dag=dag
)

dummy_operator >> hello_operator >> copy_operator >> branch_operator

a_operator = PythonOperator(task_id="xcom_push", python_callable=xcom_push, dag=dag)

next_job = PythonOperator(
    task_id="next_job",
    python_callable=last_function,
    trigger_rule="one_success",
    dag=dag,
)

b_operator = PythonOperator(
    task_id="b_data", python_callable=b_data, dag=dag
)  # DummyOperator(task_id='t' + option, dag=dag)

for option in options:
    if option == "xcom_push":
        # branch_operator >> a_operator >> next_job
        branch_operator >> a_operator >> next_job
        continue
    # elif fall_test == 'b_data':
    # branch_operator >> b_operator >> next_job
    elif option != "xcom_push":
        t = DummyOperator(task_id="t_dummy", dag=dag)
        # branch_operator	>> t
        branch_operator >> t >> b_operator >> next_job
        continue
    else:
        branch_operator >> next_job
