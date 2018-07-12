FROM openaigym:latest

USER root

RUN    pip install --upgrade pip && \
       pip install gym && \
       pip install numpy && \
       pip install pandas && \
       pip install matplotlib && \
       pip install jupyter

USER $NB_USER


RUN  mkdir $HOME/src

WORKDIR /src
ENTRYPOINT bash