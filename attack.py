
from socket import *
from select import *
import sys
from time import ctime

HOST = '127.0.0.2'
PORT = 10000
BUFSIZE = 1024
ADDR = (HOST, PORT)

try:
    while (1):
        clientSocket = socket(AF_INET, SOCK_STREAM)  # 서버에 접속하기 위한 소켓을 생성한다.
        clientSocket.connect(ADDR)  # 서버에 접속을 시도한다.
        clientSocket.send("attack".encode())  # 서버에 메시지 전달

except Exception as e:
    print('%s:%s' % ADDR)
    sys.exit()

print('connect is success')
