FROM debian:jessie

RUN apt-get -y update
RUN apt-get -y install wget curl libatlas-base-dev libatlas3-base libopenmpi-dev openmpi-bin libssl-dev build-essential libncurses5 libncurses5-dev zip uuid-dev libfreetype6-dev tk-dev libhdf5-dev mercurial libzmq-dev libsqlite3-dev gfortran

USER root
RUN groupadd dedalus && useradd -r -g dedalus dedalus
RUN echo "dedalus:dedalus" | chpasswd
RUN mkdir /home/dedalus
RUN chown -R dedalus:dedalus /home/dedalus

WORKDIR /var
RUN wget https://bitbucket.org/dedalus-project/dedalus/raw/tip/docs/install.sh
RUN chown -R dedalus:dedalus /var

USER dedalus
WORKDIR /var
RUN bash install.sh
