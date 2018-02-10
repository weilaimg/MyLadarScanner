from socket import *

def Hex_To_Dec(dhex):
    dec = 0
    i=0
    while dhex[i]!='\0':
        print(dhex[i],end='')
        i = i+1
    i=0
    while dhex[i]!='\0':
        dhex[i] = str(dhex[i])
        if (dhex[i]>='0' and dhex[i]<='9'):
            dec = dec*16+int(dhex[i])
        if(dhex[i]>='A' and dhex[i]<='F'):
            dec = dec*16+int(ord(dhex[i])-ord('A')+10)
        i=i+1
    print(' ')
    return dec


serverName = 'weilaimg.cn'
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = 'abc'
clientSocket.send(bytes(sentence,encoding="utf8"))


i = 0
while (i <= 123):
    str1 = clientSocket.recv(1)
    print(str(str1,encoding="utf8"),end=''),
    i=i+1

span_num = 0
hex_loc = 0
poi_loc = 0
hex_value  = [0,1,2,3,4,5]

while span_num<1141:
    RecvBuf = str(clientSocket.recv(1),encoding='utf8')
    if(RecvBuf != ' '):
        hex_value[hex_loc] = RecvBuf
        hex_loc=hex_loc+1
    else:
        span_num = span_num+1
        #hex_loc = hex_loc+1
        hex_value[hex_loc]='\0'

        hex_loc = 0

        now_cur = span_num*0.1667-5-0.1667
        
        hex_loc = 0
        now_dis = Hex_To_Dec(hex_value)

        print("Cur = %f , Dis = %d"%(now_cur,now_dis))


clientSocket.close()
