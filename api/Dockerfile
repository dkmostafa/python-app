FROM ubuntu:latest
FROM python:latest

WORKDIR /project
ADD . /project

ADD requirements.txt /project/

RUN pip install --user -r /project/requirements.txt

EXPOSE 5000
CMD ["python","app.py"]
