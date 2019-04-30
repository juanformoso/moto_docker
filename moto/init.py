#!/usr/bin/env python

import os

from boto import sns as botosns
from boto import sqs as botosqs

AWS_REGION = "us-east-1"
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")


def init_queue(name):
    conn = __get_connection(botosqs)
    q = conn.get_queue(name)
    if not q:
        conn.create_queue(name)


def init_topic(name):
    __get_connection(botosns).create_topic(name)


def __get_connection(service):
    return service.connect_to_region(
        AWS_REGION,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )


def __init_entities(env_var_name, init_entity_function):
    names = os.getenv(env_var_name)
    if names:
        for name in names.split(","):
            init_entity_function(name)


# SQS initialization
__init_entities("SQS_INIT_QUEUES", init_queue)

# SNS initialization
__init_entities("SNS_INIT_TOPICS", init_topic)

# add initialization for more services as needed
