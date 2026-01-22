ARG BASE_IMAGE=python:3.11-slim
FROM ${BASE_IMAGE}

WORKDIR /app

COPY base-requirements.txt .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy existing project code (unchanged)
COPY . /app
