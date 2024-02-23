import yaml
import os

def load_config(config_path='config/default_config.yaml'):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    # Override with environment variables, if exist
    config['kafka']['broker'] = os.getenv('FAUSTREAM_KAFKA_BROKER', config['kafka']['broker'])
    config['kafka']['topic'] = os.getenv('FAUSTREAM_KAFKA_TOPIC', config['kafka']['topic'])
    config['kafka']['prediction_topic'] = os.getenv('FAUSTREAM_KAFKA_PREDICTION_TOPIC', config['kafka']['prediction_topic'])
    config['model']['path'] = os.getenv('FAUSTREAM_MODEL_PATH', config['model']['path'])

    return config

