from kafka import KafkaConsumer
import json
from tqdm import tqdm

# Kafka 컨슈머 생성
consumer = KafkaConsumer(
    'topic1',  # 구독할 토픽 이름
    bootstrap_servers=['localhost:9092'],  # Kafka 브로커 주소
    auto_offset_reset='earliest',  # 가장 오래된 메시지부터 읽기
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),  # JSON 역직렬화
    consumer_timeout_ms=5000  # 타임아웃 설정
)

print('[start] get consumer')

# 메시지 읽기 및 출력
for msg in tqdm(consumer, desc="Reading messages", unit="msg"):
    print(msg.value)

print('[End] get consumer')

