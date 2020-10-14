#!/usr/bin/env python

import os

from boto import sns as botosns
from boto import sqs as botosqs

AWS_REGION = "us-east-1"
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")


def topic_to_arn(topic):
    return "arn:aws:sns:us-east-1:123456789012:{}".format(topic)


def get_connection(service):
    return service.connect_to_region(
        AWS_REGION,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )


def init_queue(name):
    conn = get_connection(botosqs)
    q = conn.get_queue(name)
    if not q:
        visibility_timeout = os.getenv("SQS_VISIBILITY_TIMEOUT")
        if visibility_timeout is not None:
            visibility_timeout = int(visibility_timeout)
        print(f"Creating queue {name} with visibility_timeout={visibility_timeout}")
        conn.create_queue(name, visibility_timeout=visibility_timeout)


def init_topic(name):
    print(f"Creating sns topic {name}")
    get_connection(botosns).create_topic(name)


def subscribe_sqs_to_sns(sqs_to_sns):
    print(f"Subscribing {sqs_to_sns}")
    sqs, sns_topic = sqs_to_sns.split("@")
    q = get_connection(botosqs).get_queue(sqs)
    get_connection(botosns).subscribe_sqs_queue(topic_to_arn(sns_topic), q)


def init_entities(env_var_name, init_entity_function):
    names = os.getenv(env_var_name, [])
    if names:
        names = names.split(",")

    for name in names:
        init_entity_function(name)


# SQS initialization
init_entities("SQS_INIT_QUEUES", init_queue)

# SNS initialization
init_entities("SNS_INIT_TOPICS", init_topic)

# SQS to SNS subscriptions
init_entities("SQS_TO_SNS_SUBSCRIPTIONS", subscribe_sqs_to_sns)

# add initialization for more services as needed
