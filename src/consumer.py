import json
import psycopg2
from kafka import KafkaConsumer
from datetime import datetime

consumer = KafkaConsumer(
    "user_events",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    auto_offset_reset="earliest",
    enable_auto_commit=True,
)

conn = psycopg2.connect(
    host="localhost",
    database="events_db",
    user="postgres",
    password="postgres"
)
cur = conn.cursor()

print("📥 Consuming events and loading into Postgres...")

for message in consumer:
    event = message.value

    cur.execute(
        """
        INSERT INTO user_events (user_id, event_type, event_time, metadata)
        VALUES (%s, %s, %s, %s)
        """,
        (
            event["user_id"],
            event["event_type"],
            datetime.fromisoformat(event["event_time"]),
            json.dumps(event["metadata"])
        )
    )

    conn.commit()
    print("Inserted:", event)
