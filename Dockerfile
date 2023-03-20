FROM python:3.9-slim-buster

WORKDIR /usr/src/app

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements file and install dependencies
COPY services/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY services/web .

# Expose port and run application
EXPOSE 5000
CMD ["python", "manage.py", "run", "-h", "0.0.0.0", "-p", "5000"]