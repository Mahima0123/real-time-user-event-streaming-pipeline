import json
import time
import random
from datetime import datetime
from kafka import KafkaProducer
from faker import Faker

fake = Faker()

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

EVENT_TYPES = ["login", "click", "logout", "purchase"]

def generate_event():
    return {
        "user_id": random.randint(1, 1000),
        "event_type": random.choice(EVENT_TYPES),
        "event_time": datetime.utcnow().isoformat(),
        "metadata": {
            "ip": fake.ipv4(),
            "device": random.choice(["mobile", "desktop", "tablet"])
        }
    }

print("Streaming events to Kafka...")

while True:
    event = generate_event()
    producer.send("user_events", event)
    print("Sent:", event)
    time.sleep(2)
