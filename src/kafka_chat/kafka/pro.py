from kafka import KafkaProducer
import time
import json
from tqdm import tqdm

pro = KafkaProducer(
    bootstrap_servers=['localhost:9092'], # KafkaProducer 객체가 localhost:9092에서 실행 중인 Kafka 브로커에 연결
    value_serializer=lambda x: json.dumps(x).encode('utf-8') # json형식으로 데이터 직렬화
)

start = time.time()

for i in tqdm(range(10)):
    data = {'str': 'value' + str(i)}
    pro.send('topic1', value=data)
    time.sleep(1)
    pro.flush() # 성공적으로 전송될 때까지 대기

end = time.time()
print("[DONE]:", end - start) # 종료 시간을 기록하고, 전체 실행 시간(시작 시간과 종료 시간의 차이)을 출력

