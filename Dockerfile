FROM ubuntu:18.04

# upgrade installed packages
RUN apt-get update && apt-get upgrade -y && apt-get clean

# needed for the bootstrap script
RUN apt-get install netcat -y

# python package management and basic dependencies
RUN apt-get install -y python-setuptools python-dev python-pip

# install moto server
RUN pip --no-cache-dir install "moto[server]"

# copy dependency files
WORKDIR /moto
COPY moto/* ./
RUN chmod u+x /moto/bootstrap.sh

EXPOSE 5000

CMD ["/moto/bootstrap.sh"]
