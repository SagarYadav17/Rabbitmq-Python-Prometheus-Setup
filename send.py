#!/usr/bin/env python
import pika
from datetime import datetime
from time import sleep

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue="hello")

while True:
    theTime = {"time": datetime.now().strftime("%H:%M:%S")}

    sleep(1)
    print("send", theTime)

    channel.basic_publish(
        exchange="",
        routing_key="hello",
        body=str(theTime),
    )
