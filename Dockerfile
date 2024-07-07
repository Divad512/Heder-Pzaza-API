# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Create a directory for the JSON files and copy them
#RUN mkdir -p /app/Json
#COPY Json/Ac.json /app/Json/Ac.json
#COPY Json/Alarm.json /app/Json/Alarm.json
#COPY Json/data.json /app/Json/data.json
#COPY Json/Light.json /app/Json/Light.json

# Expose port 8000 to the world outside this container
#EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5127"]
