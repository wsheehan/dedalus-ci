FROM alpine:latest
MAINTAINER Will Sheehan

RUN adduser -D jenkins && mkdir /var/jenkins_home && chown -R jenkins:jenkins /var/jenkins_home
RUN mkdir -p /var/log/jenkins && chown -R jenkins:jenkins /var/log/jenkins

VOLUME ["/var/log/jenkins", "/var/jenkins_home"]

USER jenkins
CMD ["/bin/sh"]