import os
from functools import wraps
import pandas as pd
from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator,ShortCircuitOperator
from dotenv import dotenv_values
from sqlalchemy import create_engine, inspect
from datetime import datetime,timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

args = {
    "owner": "Airflow",
    "start_date": datetime(2023, 1, 1), 
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)}


DATASET_URL = "D:/tenacademy/new/Airflow/data/data.csv"


CONFIG = dotenv_values(".env")

def connect_db():
    print("Connecting to DB")
    connection_uri = "postgresql://{}:{}@{}:{}/{}".format(
        CONFIG["POSTGRES_USER"],
        CONFIG["POSTGRES_PASSWORD"],
        CONFIG['POSTGRES_HOST'],
        CONFIG["POSTGRES_PORT"],
        CONFIG["POSTGRES_DB"],
    )

    engine = create_engine(connection_uri, pool_pre_ping=True)
    engine.connect()
    return engine



def extract_data(DATASET_URL):
    print(f"Reading dataset from {DATASET_URL}")
    df = pd.read_csv(DATASET_URL)
    return df



def check_table_exists(table_name, engine):
    if table_name in inspect(engine).get_table_names():
        print(f"{table_name!r} exists in the DB!")
    else:
        print(f"{table_name} does not exist in the DB!")


def load_to_db(df, table_name, engine):
    print(f"Loading dataframe to DB on table: {table_name}")
    df.to_sql(table_name, engine, if_exists="replace")


def tables_exists():
    db_engine = connect_db()
    print("Checking if tables exists")
    check_table_exists("df_trafic1", db_engine)
    db_engine.dispose()


def etl():
    db_engine = connect_db()
    raw_df = extract_data(DATASET_URL)
    raw_table_name = "df_trafic1"
    load_to_db(raw_df, raw_table_name, db_engine)
    db_engine.dispose()


DBT_CMD = "dbt"

def work_on_dbt():
    print("Work on bt")


dbt_seed = BashOperator(
    task_id='dbt_seed',
    bash_command=f"{DBT_CMD} seed --profiles-dir /dbt",
)

dbt_run = BashOperator(
    task_id='dbt_run',
    bash_command=f"{DBT_CMD} run --profiles-dir /dbt",
)

dbt_test = BashOperator(
    task_id='dbt_test',
    bash_command=f"{DBT_CMD} test --profiles-dir /dbt",
)

dbt_docs_generate = BashOperator(
    task_id='dbt_docs_generate',
    bash_command=f"{DBT_CMD} docs generate --profiles-dir /dbt",
)

DAG
with DAG('RAW-DATA-EXTRACTOR-AND-LOADER',start_date = datetime(2023, 1, 1), catchup=False, schedule_interval = '@daily') as dag:
  
    checking_db_connection = ShortCircuitOperator(
        task_id='Connecting_to_DB',
        python_callable=connect_db,
    )
    creating_db = ShortCircuitOperator(
        task_id='Reading_dataset',
        python_callable=extract_data,
    )
    creating_stations_table = ShortCircuitOperator(
        task_id='check_table_exists',
        python_callable=check_table_exists,
    )

    work_on_dbt = ShortCircuitOperator(
        task_id='work_on_dbt',
        python_callable=work_on_dbt,
    )


    dbt_tasks = [dbt_seed, dbt_run, dbt_test, dbt_docs_generate]

    checking_db_connection >> creating_db >> creating_stations_table >> work_on_dbt >> dbt_tasks
