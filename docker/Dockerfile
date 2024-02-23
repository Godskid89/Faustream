FROM python:3.8-slim

WORKDIR /usr/src/app

# Install Python and pip requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install yq for YAML processing (optional based on your start.sh approach)
# RUN pip install yq

# for start.sh, install PyYAML
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
