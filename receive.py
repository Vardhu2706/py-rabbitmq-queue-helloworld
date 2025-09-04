import pika, sys, os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    
    channel.queue_declare(queue='hello')
    
    def callback(ch, method, properties, body):
        print(f" [Y] Received {body}, Channel: {ch}, Method: {method}, Properties: {properties}")
        
    channel.basic_consume(queue='hello',
                          on_message_callback=callback,
                          auto_ack=True)
    
    print(f" [*] Waiting for messages. To exit press CRTL+C")
    channel.start_consuming()
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)