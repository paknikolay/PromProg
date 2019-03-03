#!/usr/bin/env python
import pika
import time
import random

conn_params = pika.ConnectionParameters('rabbit', 5672)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue='queue')

for i in range(1000):
    channel.basic_publish(exchange='',
			  routing_key='queue',
			  body=str(random.randint(0,200)))
    print("send int")
    time.sleep(random.randint(0,2))

connection.close()
