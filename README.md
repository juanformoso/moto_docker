### Summary

Docker container for using moto server with ubuntu.  
Moto server is a standalone server mode of the [Moto library](https://github.com/spulec/moto), that can be used to mock AWS services.

### Getting the image

    docker pull juanformoso/moto_docker

### Running AWS services using moto_docker

    docker run --name moto -d -i juanformoso/moto_docker

### Example with docker-compose

    version: '3'

    moto:
      image: juanformoso/moto_docker
      ports:
        - "5000:5000"

### Using it with an application

If you are using the boto library, you can then specify the necessary settings [using a configuration file](http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto)

    export BOTO_CONFIG=./boto.conf

Where `boto.conf` contains the following

    [Boto]
    is_secure = False
    https_validate_certificates = False
    proxy = moton
    proxy_port = 5000
    
