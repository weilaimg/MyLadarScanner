from socket import *
import json

def Generator_Json_Str():
    Json_Dic = {'Height':20,
                'Km_Sign':1500,
                'Timing':300,
                'Dis_Start':2.0,
                'Dis_End':4.0,
                'Cur_Start':60,
                'Cur_End':120
                }
    
    return json.dumps(Json_Dic)

if __name__ == "__main__":
    
    serverName = 'weilaimg.cn'
    serverPort = 10020
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    i = input("Please input I :")
    clientSocket.send(bytes(i,encoding="utf8"))

    print(str(clientSocket.recv(1024),encoding="utf8"))

    sentence = Generator_Json_Str()
    print(sentence)
    clientSocket.send(bytes(sentence,encoding="utf8"))

    print(str(clientSocket.recv(1024),encoding="utf8"))
    
    t=0

    while 1:
        str1 = clientSocket.recv(1024)
        print(str(str1,encoding="utf8"))
        t = t+1

    i = input("Please input I :")
    clientSocket.send(bytes(i,encoding="utf8"))

    print(str(clientSocket.recv(1024),encoding="utf8"))
    print(str(clientSocket.recv(1024),encoding="utf8"))
    #clientSocket.send(bytes('asd',encoding="utf8"))
    

    clientSocket.close()
    
