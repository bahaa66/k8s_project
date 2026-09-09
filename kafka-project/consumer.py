from confluent_kafka import Consumer

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'test-group'
})

consumer.subscribe(['test'])

while True:
    message = consumer.poll(1)

    if message is not None:
        print(message.value().decode())
        print("offset:", message.offset())