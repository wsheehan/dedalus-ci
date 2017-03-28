FROM dedalusproject/dedalus-app:latest

USER root
RUN apt-get -y install openssh-server default-jre default-jdk
RUN sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd
RUN mkdir -p /var/run/sshd

# Copy bash scripts & assets
WORKDIR /home/dedalus
COPY build_steps build_steps

RUN pip3 install docopt

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
