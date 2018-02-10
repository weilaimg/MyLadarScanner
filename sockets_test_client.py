from socket import *
import math
def Hex_To_Dec(dhex):
    dec = 0
    i=0
    while dhex[i]!='\0':
        if (dhex[i]>='0' and dhex[i]<='9'):
            dec = dec*16+int(dhex[i])
        if(dhex[i]>='A' and dhex[i]<='F'):
            dec = dec*16+int(ord(dhex[i])-ord('A')+10)
        i=i+1
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
    i=i+1

span_num = 0
hex_loc = 0
poi_loc = 0
hex_value  = ['','','','','','']
Point_List=[]
while span_num<1141:
    RecvBuf = str(clientSocket.recv(1),encoding='utf8')
    if(RecvBuf != ' '):
        hex_value[hex_loc] = RecvBuf
        hex_loc=hex_loc+1
    else:
        span_num = span_num+1
        hex_value[hex_loc]='\0'

        hex_loc = 0

        now_cur = span_num*0.1667-5-0.1667
        
        hex_loc = 0
        now_dis = Hex_To_Dec(hex_value)

        now_dagao = now_dis*math.sin(now_cur*(math.pi/180))
        now_lachu = now_dis*math.cos(now_cur*(math.pi/180))
        
        if now_dis>3000 and now_dis<3200 and now_cur>60 and now_cur<120:
            Point_dic=dict()
            Point_dic['now_dis']=now_dis
            Point_dic['now_cur']=now_cur
            Point_dic['now_dagao']=now_dagao
            Point_dic['now_lachu']=now_lachu
            Point_List.append(Point_dic)
print(Point_List)
if len(Point_List)>45 or len(Point_List)==0:
    pass
else:
    pass


clientSocket.close()
