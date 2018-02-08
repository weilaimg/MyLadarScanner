from socket import *
import threading 
import time 
import json
import random

class MyLadarScanner:
    def Start_Listening(self,Server_Port):
        self.serverSocket = socket(AF_INET,SOCK_STREAM)
        self.serverSocket.bind(('',Server_Port))
        self.serverSocket.listen(1)
        self.Recv_Sign = 0

    def Get_Socket_Connect(self):
        self.connectionSocket, self.addr = self.serverSocket.accept()
        self.daogao1 = 4850
        self.daogao2 = 4620
        self.lachu1 = 300
        self.lachu2 = -300
        self.speed = 15.0
        self.j1 = True
        self.j2 = True

    def Get_Recv_Str(self,rwnd):
        Rec_Str = self.connectionSocket.recv(rwnd)
        return str(Rec_Str,encoding="utf8")

    def Check_Recv_Str(self,rwnd):
        Rec_Str = self.connectionSocket.recv(rwnd)
        self.Rec_Str = str(Rec_Str,encoding="utf8")
        self.Recv_Sign = 1

    def Send_Socket_Data(self,Send_Data):
        self.connectionSocket.sendall(bytes(Send_Data,encoding="utf8"))

    def Set_Init_Data(self,Height,Km_Sign,Timing,Dis_Start,Dis_End,Cur_Start,Cur_End):
        self.Height = Height
        self.Km_Sign = Km_Sign
        self.Timing = Timing
        self.Dis_Start = Dis_Start
        self.Dis_End = Dis_End
        self.Cur_Start = Cur_Start
        self.Cur_End = Cur_End

    def Sep_Initial_Data(self,Json_Str):
        flag = 0
        try:
            Json_Dic = json.loads(Json_Str)
            Height = Json_Dic['Height']
            Km_Sign = float(Json_Dic['Km_Sign'])
            Timing = float(Json_Dic['Timing'])/1000
            Dis_Start = Json_Dic['Dis_Start']
            Dis_End = Json_Dic['Dis_End']
            Cur_Start = Json_Dic['Cur_Start']
            Cur_End = Json_Dic['Cur_End']
            flag = 1
            self.Set_Init_Data(Height,Km_Sign,Timing,Dis_Start,Dis_End,Cur_Start,Cur_End)
        except:
            flag = 0
        return flag

    def Stop_Listening(self):
        self.connectionSocket.close()

    def Send_All_Data(self):
        self.speed = 15.0
        self.lachu1 = self.Get_Next_Lachu1(self.lachu1) + random.randint(-15,15)
        self.lachu2 = self.Get_Next_Lachu2(self.lachu2) + random.randint(-15,15)
        self.daogao1 = self.daogao1 + random.randint(-30,30)
        self.daogao2 = self.daogao2 + random.randint(-30,30)
        self.speed = self.speed + float(random.randint(-15,15))/3
        self.Km_Sign = self.Km_Sign + self.speed*self.Timing
        Send_Data = self.Gen_Send_Json()
        self.Send_Socket_Data(Send_Data)

    def Get_Next_Lachu1(self,i):
        if i <-550:
            self.j1 = False
        elif i >550:
            self.j1 = True

        if self.j1:
            return i-15
        else :
            return i+15

    def Get_Next_Lachu2(self,i):
        if i <-550:
            self.j2 = False
        elif i >550:
            self.j2 = True

        if self.j2:
            return i-15
        else :
            return i+15

    def Gen_Send_Json(self):
        Json_Dic = {'lachu1':self.lachu1,
                    'lachu2':self.lachu2,
                    'daogao1':self.daogao1,
                    'daogao2':self.daogao2,
                    'speed':float(str("%.2f"%self.speed)),
                    'Km_Sign':float(str("%.2f"%self.Km_Sign))}
        return json.dumps(Json_Dic)

if __name__ == '__main__':

    My = MyLadarScanner()

    My.Start_Listening(10020)
   
    while True:

        My.Get_Socket_Connect()

        t = threading.Thread(target = My.Check_Recv_Str,args=(1024,))
        t.start()
        while My.Recv_Sign == 0:
            pass
        My.Recv_Sign = 0
        if My.Rec_Str == '':
            My.Stop_Listening()
            continue
        My.Send_Socket_Data("Server side is ready")



        t = threading.Thread(target = My.Check_Recv_Str,args=(1024,))
        t.start()
        while My.Recv_Sign == 0:
            pass
        My.Recv_Sign = 0
        if My.Rec_Str == '':
            My.Stop_Listening()
            continue
        Json_Str = My.Rec_Str

        if My.Sep_Initial_Data(Json_Str) == 1 :
            pass
        else:
            My.Send_Socket_Data("Error")
            continue
        

        t = threading.Thread(target = My.Check_Recv_Str,args=(1024,))
        t.start()
        while My.Recv_Sign == 0:
            try:
                My.Send_All_Data()
                time.sleep(My.Timing)
            except:
                pass

        My.Recv_Sign = 0
        try:
            My.Send_Socket_Data("Server side is closed")
        except:
            pass
        if My.Rec_Str == '':
            My.Stop_Listening()
            continue

        My.Stop_Listening()







