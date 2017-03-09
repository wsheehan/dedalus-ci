FROM nginx:1.10
MAINTAINER Will Sheehan

RUN rm /etc/nginx/conf.d/default.conf
RUN rm /etc/nginx/nginx.conf

COPY conf/jenkins.conf /etc/nginx/conf.d/jenkins.conf
COPY conf/nginx.conf /etc/nginx/nginx.conf

RUN mkdir /etc/secrets
COPY conf/myssl.crt /etc/secrets/proxycert.crt
COPY conf/myssl.key /etc/secrets/proxykey.key
