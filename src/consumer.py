from kafka import KafkaConsumer
import config

config = config.load_config()
# Configuration
# bootstrap_servers = [config['kafka']['broker']]  # e.g., ['localhost:9092']
# prediction_topic = config['kafka']['topic']

bootstrap_servers = ['localhost:9092']
prediction_topic = 'output_topic'

# Initialize consumer
consumer = KafkaConsumer(
    prediction_topic,
    bootstrap_servers=bootstrap_servers,
    auto_offset_reset='earliest',  # Start reading at the earliest message
    group_id='my-consumer-group'  # Use a unique group ID
)

# Consume messages
for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}")
