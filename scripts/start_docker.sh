#!/bin/bash

cd "$(dirname "$0")"

source export_config.sh

# Navigate to the directory containing your docker-compose.yml file
cd ..

# Run docker-compose up
docker-compose up
