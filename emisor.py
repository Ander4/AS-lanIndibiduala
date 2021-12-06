#/usr/bin/env python
import pika

credentials = pika.PlainCredentials(username='guest', password='guest')
parameters= pika.ConnectionParameters('rabbitmq', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Enhorabuena, eres el cliente 1.000.000, pincha en el siguiente enlace para reclamar tu premio: https://www.youtube.com/watch?v=dQw4w9WgXcQ')
print(" [x] Sent 'Hola Mundo'")
connection.close()
