FROM juanformoso/ubuntu_python3_base
LABEL maintainer="Juan Manuel Formoso <jformoso@gmail.com>"
LABEL project="moto_docker"
LABEL description="Docker image to use moto with ubuntu"

# needed for the bootstrap script
RUN apt-get install netcat -y

# install moto server
RUN pip --no-cache-dir install moto[server]==1.3.14

# copy dependency files
WORKDIR /moto
COPY moto/* ./
RUN chmod u+x /moto/bootstrap.sh

EXPOSE 5000

CMD ["/moto/bootstrap.sh"]
