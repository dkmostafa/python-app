FROM ubuntu:latest
FROM jupyter/base-notebook

USER root
RUN apt-get update

ADD requirements.txt /code/
RUN pip install -U -r /code/requirements.txt

RUN conda install --quiet --yes -c \
    conda-forge osmnx dask
RUN conda install mysql-connector-python




RUN fc-cache
RUN fc-list

VOLUME /notebooks
WORKDIR /notebooks
