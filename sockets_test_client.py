from socket import *
serverName = 'weilaimg.cn'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = 'abc'
clientSocket.send(sentence)
i = 5000
while(i > 0):
    str1 = clientSocket.recv(1)
    print(str1),
    i=i-1

clientSocket.close()
