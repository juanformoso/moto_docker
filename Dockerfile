FROM ubuntu:18.04

# Upgrade installed packages
RUN apt-get update && \
	apt-get upgrade -y && \
	apt-get clean

# Python package management and basic dependencies
RUN apt-get install -y python-setuptools python-dev python-pip

RUN  pip --no-cache-dir install "moto[server]"

ENTRYPOINT ["moto_server", "-H", "0.0.0.0"]

EXPOSE 5000
