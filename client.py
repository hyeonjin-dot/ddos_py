#! /usr/bin/python
# -*- coding: utf-8 -*-

from socket import *
from select import *
import sys
from time import ctime

HOST = '127.0.0.3'
PORT = 10000
BUFSIZE = 1024
ADDR = (HOST, PORT)

print('stopserver를 입력할시 서버와 클라이언트 종료')
try:
    while (1):
        clientSocket = socket(AF_INET, SOCK_STREAM)  # 서버에 접속하기 위한 소켓을 생성한다.
        message = input("서버에 보낼 메세지 입력")
        clientSocket.connect(ADDR)  # 서버에 접속을 시도한다.
        clientSocket.send(message.encode())  # 서버에 메시지 전달
        if (message == 'stopserver'):
            break

except Exception as e:
    print('%s:%s' % ADDR)
    sys.exit()

print('connect is success')
