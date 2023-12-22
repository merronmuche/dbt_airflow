FROM python:3.10.9
RUN pip install apache-airflow[postgres]==2.1.3
RUN pip install dbt
RUN pip install SQLAlchemy==1.3.23
WORKDIR /project
COPY requirements.txt /project/requirements.txt
RUN pip install -r requirements.txt
COPY . /project/
RUN chmod +x /project/scripts_airflow/init.sh
# ENTRYPOINT [ "/project/scripts_airflow/init.sh" ]

CMD airflow scheduler & airflow webserver