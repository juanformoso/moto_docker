### Summary

Docker container for using moto server with ubuntu.  
Moto server is a standalone server mode of the [Moto library](https://github.com/spulec/moto), that can be used to mock AWS services.

Docker image hosted in https://hub.docker.com/r/juanformoso/moto_docker/

### Getting the image

    docker pull juanformoso/moto_docker

### Running AWS services using moto_docker

    docker run --name moto -p 5000:5000 -d -i juanformoso/moto_docker

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
    proxy = moto
    proxy_port = 5000
    
### SQS initialization

There's a way to initialize queues on start up, this is useful so your application does not need to check if they exist and create them itself (as it assumes the queues will be created in amazon in other environments)

Just pass a comma separated list of queue names to create in the environment variable `SQS_INIT_QUEUES`

    docker run --env SQS_INIT_QUEUES=queue1,queue2 --name moto -p 5000:5000 -d -i juanformoso/moto_docker
