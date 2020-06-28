FROM puckel/docker-airflow:latest

ADD requirements.txt /code/
RUN pip install --user -r /code/requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:${AIRFLOW_HOME}"
