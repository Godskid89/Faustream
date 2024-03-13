FROM python:3.11

WORKDIR /usr/src/app

# Install Java (required for Kafka)
RUN apt-get update && apt-get install -y default-jdk && rm -rf /var/lib/apt/lists/*

# Install dependencies for downloading and extracting Kafka
RUN apt-get update && apt-get install -y wget tar && rm -rf /var/lib/apt/lists/*

# Download and extract Kafka to use the command-line tools
RUN wget https://downloads.apache.org/kafka/3.6.1/kafka_2.13-3.6.1.tgz -O /tmp/kafka.tgz \
    && tar -xzf /tmp/kafka.tgz -C /opt \
    && rm /tmp/kafka.tgz

# Adding Kafka bin to PATH
ENV PATH="/opt/kafka_2.13-3.6.1/bin:${PATH}"

# Install Python and pip requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Optionally, install yq for YAML processing if your start.sh script requires it
# RUN pip install yq

# For start.sh, install PyYAML if you're manipulating YAML files in your scripts
# RUN pip install pyyaml

# Copy the current directory contents into the container at /usr/src/app
COPY src/ ./src
COPY models/ ./models
COPY config/ ./config
COPY scripts/ ./scripts

RUN chmod +x ./scripts/start.sh

# Expose port 6066 for your application (if necessary)
EXPOSE 6066

# Use the start.sh script to start the container
CMD ["./scripts/start.sh"]
