#!/bin/bash

CONFIG_FILE="/config/default_config.yaml"

# Function to get Kafka broker from the configuration file
get_kafka_broker() {
    python -c "import yaml; print(yaml.safe_load(open('$CONFIG_FILE'))['kafka']['broker'])"
}

# Set the KAFKA_BROKER variable
KAFKA_BROKER=$(get_kafka_broker)

# Check if Kafka is ready
kafka_ready() {
    # Use the KAFKA_BROKER variable dynamically
    kafka-broker-list.sh --bootstrap-server $KAFKA_BROKER --list 2>/dev/null
    return $?
}

# Wait for Kafka to be ready
echo "Waiting for Kafka to be ready..."
until kafka_ready; do
  sleep 2
  echo "Retrying..."
done
echo "Kafka is ready."

# Start Faust application
faust -A src.app worker -l info
