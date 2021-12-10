#/usr/bin/env python
import pika

credentials = pika.PlainCredentials(username='guest', password='guest')
parameters= pika.ConnectionParameters('rabbitmq', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue='hello')

mensaje='Enhorabuena, eres el cliente 1.000.000, accede en el siguiente enlace para ver como reclamar tu premio: https://www.youtube.com/watch?v=dQw4w9WgXcQ'
channel.basic_publish(exchange='', routing_key='hello', body=mensaje)
print(" [x] Sent ",mensaje)
connection.close()
