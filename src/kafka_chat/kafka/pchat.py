from kafka import KafkaProducer
from json import dumps
import time

p = KafkaProducer(
	bootstrap_servers=['localhost:9092'],  # Kafka 브로커 주소 지정 -> 브로커레 연결
	value_serializer=lambda x: dumps(x).encode('utf-8')  # 메시지 직렬화
)
print("채팅프로그램 - 메세지 발신자")
print("메세지를 입력하세요. (종료 시 'exit'입력)")

while True:
	msg = input("YOU : ")
	if msg == 'exit':
	    break
	data = {'message': msg, 'time' : time.time()} # 딕셔너리로 반환
	# 메세지 발송
	p.send('chat', value=data) # 인스턴스 p를 이용해 Kafka 토픽에 data를 전송. value는 직렬화된 메시지 데이터
	
print("채팅 종료")
p.close()
