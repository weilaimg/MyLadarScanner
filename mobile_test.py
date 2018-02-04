from socket import *
serverPort = 10000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen()
print ('The server is ready to receive')
while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.upper()
    print(addr)
    connectionSocket.send(capitalizedSentence)
    i=0
    while i<10:
        connectionSocket.send(bytes("sadf",encoding="utf8"))
        i = i+1
    connectionSocket.close()
