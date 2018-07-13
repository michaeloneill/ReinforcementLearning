FROM openaigymbase:latest

USER root

RUN    apt-get update && \
       apt-get install -y python3-pip python3-dev xvfb emacs && \
       cd /usr/local/bin && \
       ln -s /usr/bin/python3 python && \
       pip3 install gym && \
       pip3 install numpy && \
       pip3 install pandas && \
       pip3 install matplotlib && \
       pip3 install jupyter

ENV    NB_USER rl_user
ENV    NB_GROUP rl_users
ENV    NB_UID 1000
ENV    NB_GID 1001
ENV    HOME /home/$NB_USER

RUN     useradd -m -s /bin/bash -N -u $NB_UID $NB_USER  && \
        groupadd -g $NB_GID $NB_GROUP && \
	usermod -g $NB_GROUP $NB_USER && \
	echo "umask g+rwx" >> /root/.bashrc && \
	echo "umask g+rwx" >> $HOME/.bashrc

# Setup correct permissions on important folders in docker container
RUN     mkdir /src
RUN     chown -R $NB_USER:$NB_GROUP /src
RUN     chmod -R g+rw /src

USER $NB_USER

WORKDIR /src/

ENTRYPOINT bash