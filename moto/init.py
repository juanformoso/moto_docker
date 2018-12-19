#!/usr/bin/env python

import os
from boto import sqs as botosqs

AWS_REGION = "us-east-1"
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")


def init_queue(name):
    conn = botosqs.connect_to_region(
        AWS_REGION,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )
    q = conn.get_queue(name)
    if not q:
        conn.create_queue(name)

# SQS initialization
queue_names = os.getenv('SQS_INIT_QUEUES')
if queue_names:
    for name in queue_names.split(','):
        init_queue(name)

# add initialization for more services as needed
