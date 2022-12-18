from socket import *
from select import *
import time


HOST = ''
PORT = 10000
BUFSIZE = 1024
ADDR = (HOST, PORT)
Host = {}
denied = []
# 소켓 생성
serverSocket = socket(AF_INET, SOCK_STREAM)
# 소켓 주소 정보 할당
serverSocket.bind(ADDR)
print('bind')
# 연결 수신 대기 상태
serverSocket.listen(100)
print('listen')
start = time.time()
# 연결 수락
k = 0
while (1):

    clientSocekt, addr_info = serverSocket.accept()
    for i in denied:
        if ((clientSocekt.getsockname()[0]) == i):
            clientSocekt.close()
            k = 1

    if (k == 1):
        k=0
        continue
    if (clientSocekt.getsockname()[0] in Host):

        Host[clientSocekt.getsockname()[0]] = Host[clientSocekt.getsockname()[0]]+1
        data = clientSocekt.recv(65535)

    else:
        Host[clientSocekt.getsockname()[0]] = 1
        data = clientSocekt.recv(65535)

 # 클라이언트로부터 메시지를 가져옴
    if data.decode(encoding='UTF-8', errors='strict') == 'stopserver':
        break

    print(clientSocekt.getsockname()[0])
    print('recieve data : ', data.decode())
    endtime = time.time()

    if (endtime-start >= 5):
        for key, value in Host.items():

            if (Host[key] > 100):
                Host[key] = -1
                denied.append(key)
                denied = list(set(denied))
            else:
                Host[key] = 0

        start = time.time()


# 소켓 종료
clientSocekt.close()
serverSocket.close()
print('close')
