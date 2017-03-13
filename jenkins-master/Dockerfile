FROM jenkins:alpine
MAINTAINER Will Sheehan

USER root
RUN mkdir /var/log/jenkins
RUN chown -R jenkins:jenkins /var/log/jenkins 

USER jenkins

ENV JENKINS_OPTS="--logfile=/var/log/jenkins/jenkins.log"
ENV JAVA_OPTS="-Dhudson.security.csrf.requestfield=Jenkins-Crumb"