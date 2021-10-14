# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.7-slim

# Copy local code to the container image.
WORKDIR /app
COPY . .

# Install production dependencies.
RUN pip install Flask

COPS model.pt /app

# Run the web service on container startup.
CMD ["python3", "main.py"]
