# real-time-user-event-streaming-pipeline
# Real-Time User Event Streaming Pipeline

## Overview
Built an end-to-end real-time data pipeline that simulates user activity events, streams them through Kafka, and stores them in PostgreSQL for analytics.

The project demonstrates real-world data engineering concepts such as event streaming, containerized infrastructure, and analytical querying.

## Architecture
Producer (Python + Faker)
→ Kafka
→ Consumer (Python)
→ PostgreSQL
→ SQL Analytics

## Tech Stack
- Python
- Apache Kafka
- PostgreSQL
- Docker & Docker Compose
- SQL
- kafka-python, psycopg2, Faker

## Features
- Generates realistic user events (login, logout, click, purchase)
- Streams events in real time using Kafka
- Persists data reliably into PostgreSQL
- Supports analytical queries for user behavior insights

## Sample Analytics
- Event distribution by type
- Daily active users
- Device usage patterns
- Top purchasing users

## How to Run
1. Start services:
   ```bash
   docker compose up -d
2. Run producer
    python src/producer.py
3. Run consumer
    python src/consumer.py
4. Run analytics
    docker exec -i postgres_container psql < sql/analytics.sql
