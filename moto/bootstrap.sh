#!/usr/bin/env bash

set -e

export BOTO_CONFIG=/moto/boto.conf
export AWS_ACCESS_KEY_ID=11111111111111111111
export AWS_SECRET_ACCESS_KEY=2222222222222222222222222222222222222222

nohup moto_server -H 0.0.0.0 &

# wait until the server is up and running
while ! nc -z localhost 5000 >> /dev/null 2>&1; do
    sleep 1
done

# initialization script
python init.py

tail -f /dev/null
