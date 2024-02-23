# Faustream: Real-Time Machine Learning Stream Processing Tool

Faustream is an open-source tool designed for real-time prediction on streaming data using Python, Kafka, and Faust. This tool allows for easy setup, configuration, and deployment of stream processing applications.

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Python 3.8 or higher
- Kafka and Zookeeper (if running outside Docker)
- Git (for cloning the repository)

### Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/Godskid89/Faustream.git
   cd faustream
   ```

2. **Configure Your Environment**

   Before starting, configure your application by editing the `config/default_config.yaml` file. This file contains key configurations such as Kafka broker details and the path to your predictive model.

   ```yaml
   kafka:
     broker: localhost:9092 # Update with your Kafka broker address
     topic: input_topic # Kafka topic for incoming data
     prediction_topic: prediction_topic # Kafka topic for outgoing predictions
   model:
     path: models/example_model.pkl # Path to your machine learning model
   ```

   **Note:** If you are using custom models or additional configurations, ensure they are correctly placed or specified in the configuration file.

3. **Build the Docker Image**

   Navigate to the project root directory and build the Docker image:

   To build the docker_image, first run this script to make it executeable
    ```sh
    chmod +x scripts/start_docker.sh

    ```
    Then run this script:

   ```sh
   ./scripts/start_docker.sh
   ```

### Running Faustream

After building the Docker image, start Faustream using the `start.sh` script located in the scripts folder. This script initializes the Kafka broker using the configurations set in `config/default_config.yaml` and starts the Faustream application.

```sh
./scripts/start.sh
```

This command sources your configuration, setting up environment variables, and launches the Docker Compose services, including your Faustream application, Kafka, and Zookeeper.

### Customization

- **Kafka and Faust**: Customize Kafka and Faust settings within `docker/docker-compose.yml` and `config/default_config.yaml` to match your deployment environment or performance needs.
- **Predictive Models**: Replace the placeholder model in `models/` with your trained machine learning model. Update `config/default_config.yaml` with the correct model path.

### Troubleshooting

- Ensure Docker and Docker Compose are correctly installed and updated.
- Verify Kafka is accessible and correctly configured in `default_config.yaml`.
- For issues related to model predictions, ensure your model is compatible with the prediction code in `src/model_management.py`.

### Contributing

Contributions are welcome! Please read the CONTRIBUTING.md file for guidelines on how to submit issues, feature requests, and pull requests.
