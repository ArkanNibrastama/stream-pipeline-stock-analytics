from kafka import KafkaConsumer
import json
import s3fs
import boto3
from credentials import *

consumer = KafkaConsumer(

    'stock_analytics',
    bootstrap_servers=['{/YOUR_LOCAL_DEVICE_IP}'],
    value_deserializer = lambda x : json.loads(x.decode('utf-8'))

)


conn = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_ACCESS_SECRET_KEY)

for c in consumer:

    t = c.value['time']

    conn.put_object(

            Body = json.dumps(c.value),
            Bucket = 'arkan-datalake-stream-stock-analytics',
            Key = f'stock_{t}.json'

    )