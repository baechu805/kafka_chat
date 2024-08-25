from kafka import KafkaConsumer
from json import loads

# KafkaConsumer 객체 생성
consumer = KafkaConsumer(
    'chat',  # 구독할 토픽
    bootstrap_servers=['localhost:9092'],  # Kafka 브로커 주소
    auto_offset_reset='earliest',  # 시작 오프셋 설정
    value_deserializer=lambda x: loads(x.decode('utf-8')),  # 메시지 디시리얼라이즈
    group_id='chat_group',  # 컨슈머 그룹 ID
    enable_auto_commit=True  # 자동 오프셋 커밋 활성화
)

print("채팅프로그램 - 메세지 수신")
print("메세지 대기 중")

try:
    # 메시지 수신 대기 및 처리
    for m in consumer: # 새로운 메시지가 도착하면 m에 할당
        data = m.value
        print(f"[FRIEND] {data['message']}") # data에서 'message' 키에 해당하는 값을 출력

except KeyboardInterrupt:
    print("채팅종료")

finally:
    # 예외 존재여부와 상광없이 컨슈머 종료
    consumer.close()

