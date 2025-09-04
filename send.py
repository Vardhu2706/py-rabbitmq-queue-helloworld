import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

msg = 'Hello World!'
channel.basic_publish(exchange='', 
                      routing_key='hello',
                      body=msg)
print(f" [x] Sent '{msg}'")

connection.close()