FROM juanformoso/ubuntu_python3_base

# needed for the bootstrap script
RUN apt-get install netcat -y

# install moto server
RUN pip --no-cache-dir install "moto[server]"

# copy dependency files
WORKDIR /moto
COPY moto/* ./
RUN chmod u+x /moto/bootstrap.sh

EXPOSE 5000

CMD ["/moto/bootstrap.sh"]
