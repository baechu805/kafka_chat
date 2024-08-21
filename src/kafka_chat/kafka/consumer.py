from kafka import KafkaConsumer, TopicPartition
from json import loads
import os

OFFSET_FILE = 'consumer_offset.txt'

def save_offset(offset):
    with open(OFFSET_FILE, 'w') as f:
        f.write(str(offset))

def read_offset():
    if os.path.exists(OFFSET_FILE):
        with open(OFFSET_FILE, 'r') as f:
            return int(f.read().strip())
    return None  # 파일이 없으면 None 반환

saved_offset = read_offset()
# Kafka 컨슈머 생성
consumer = KafkaConsumer(
    # 'topic1',  # 구독할 토픽 이름
    bootstrap_servers=['localhost:9092'],  # Kafka 브로커 주소
    # auto_offset_reset='earliest' if read_offset() is None else 'none',  # 저장된 오프셋이 없으면 가장 오래된 메시지부터 읽기
    value_deserializer=lambda x: loads(x.decode('utf-8')),  # JSON 형식으로 역직렬화
    consumer_timeout_ms=5000,  # 메시지 소비 대기 시간 설정 => 컨슈머가 메시지를 읽기 위해 5초 동안 대기, 메시지 도착 안 하면 루프 종료
    group_id="fbi",
    enable_auto_commit=False,  # 자동 커밋 비활성화
)

print('[start] get consumer')

if saved_offset is not None:
    p = TopicPartition('topic1', 0)  # TopicPartition 객체 생성
    consumer.assign([p])  # 특정 파티션을 컨슈머에 할당
    consumer.seek(p, saved_offset)  # 저장된 오프셋으로 시킹

# 메시지 읽기 및 출력
for m in consumer:
    print(f"offset={m.offset}, value={m.value}")
    save_offset(m.offset + 1)  # 다음 메시지를 위해 현재 오프셋 + 1 저장

print('[End] get consumer')

