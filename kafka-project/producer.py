from confluent_kafka import Producer

producer = Producer({
    'bootstrap.servers': 'localhost:9092'
})

for i in range(100):
    order = {
        'order_id': i,
        'consumer_id': i % 10,
        'quantity': i + 1
    }
    producer.produce('orders', key=str(order['order_id']), value=json.dumps(order))
    producer.flush()
    