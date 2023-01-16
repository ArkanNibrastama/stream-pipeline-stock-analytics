from dummy_realtime_data_source_API import initialization, get_data
from time import sleep
import json
from kafka import KafkaProducer

producer = KafkaProducer(

    bootstrap_servers=['{/YOUR_LOCAL_DEVICE_IP}'],
    value_serializer= lambda x : json.dumps(x).encode('utf-8')

)

# clean up the producer
producer.flush()

emiten_list = initialization()

while True:

    data = get_data(emiten_list)
    # ingest data and stream it.
    producer.send('stock_analytics', data)

    sleep(1)