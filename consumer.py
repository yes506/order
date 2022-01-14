import json
import pika
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'order.settings')
django.setup()

from user_order.models import Order, Shop

params = pika.URLParameters('amqps://adyzazjv:eX3pCl0sCOFl6iETiL5bf0fngTrkLN0j@dingo.rmq.cloudamqp.com/adyzazjv')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='order')

def callback(ch, methods, properties, body):
    print('Received in order')
    id = json.loads(body)
    print(id)
    order = Order.objects.get(id=id)
    order.deliver_finish = 1
    order.save()
    print('order deliver finished')

channel.basic_consume(queue='order', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close()