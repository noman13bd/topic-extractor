# Use Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Download the spaCy English language model
RUN python -m spacy download en_core_web_sm
# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Expose any necessary ports
EXPOSE 8000

# Run the scheduler
CMD ["python", "scheduler.py"]


