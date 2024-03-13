#!/bin/bash

# Assuming default_config.yaml is in the current directory
CONFIG_PATH="config/default_config.yaml"

# Use Python to parse the YAML file and export environment variables
export FAUSTREAM_KAFKA_BROKER=$(python -c "import yaml; print(yaml.safe_load(open('$CONFIG_FILE'))['kafka']['broker'])")
export FAUSTREAM_KAFKA_TOPIC=$(python -c "import yaml; print(yaml.safe_load(open('$CONFIG_FILE'))['kafka']['topic'])")
export FAUSTREAM_MODEL_PATH=$(python -c "import yaml; print(yaml.safe_load(open('$CONFIG_FILE'))['model']['path'])")

# Echo the variables for debugging
echo "Exported FAUSTREAM_KAFKA_BROKER=$FAUSTREAM_KAFKA_BROKER"
echo "Exported FAUSTREAM_KAFKA_TOPIC=$FAUSTREAM_KAFKA_TOPIC"
echo "Exported FAUSTREAM_MODEL_PATH=$FAUSTREAM_MODEL_PATH"
