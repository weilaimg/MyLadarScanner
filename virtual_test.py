from socket import *
import threading 
import time 
import xml.dom.minidom
import XMLGenerator as Gen

import random

class MyLadarScanner:
    def Start_Listening(self,Server_Port):
        self.serverSocket = socket(AF_INET,SOCK_STREAM)
        self.serverSocket.bind(('',Server_Port))
        self.serverSocket.listen()
        self.Recv_Sign = 0
        print ('The server is ready to receive')

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

    def Sep_Initial_Data(self,Xml_Str):
        flag = 0
        try:
            DOMTree = xml.dom.minidom.parseString(Xml_Str)
            MyLadarScanner = DOMTree.documentElement
            Initial_Data = MyLadarScanner.getElementsByTagName("Initial_Data")[0]
            Height = int(Initial_Data.getElementsByTagName("Height")[0].childNodes[0].data)
            Km_Sign = float(Initial_Data.getElementsByTagName("Km_Sign")[0].childNodes[0].data)
            Timing = float(Initial_Data.getElementsByTagName("Timing")[0].childNodes[0].data)/1000
            Dis_Start = float(Initial_Data.getElementsByTagName("Dis_Start")[0].childNodes[0].data)
            Dis_End = float(Initial_Data.getElementsByTagName("Dis_End")[0].childNodes[0].data)
            Cur_Start = int(Initial_Data.getElementsByTagName("Cur_Start")[0].childNodes[0].data)
            Cur_End = int(Initial_Data.getElementsByTagName("Cur_End")[0].childNodes[0].data)
            flag = 1
            self.Set_Init_Data(Height,Km_Sign,Timing,Dis_Start,Dis_End,Cur_Start,Cur_End)
        except:
            flag = 0
        return flag

    def Stop_Listening(self):
        self.connectionSocket.close()

    def Send_All_Data(self):
        self.speed = 15.0
        self.lachu1 = self.Get_Next_Lachu1(self.lachu1)
        self.lachu2 = self.Get_Next_Lachu2(self.lachu2)
        self.daogao1 = self.daogao1 + random.randint(-30,30)
        self.daogao2 = self.daogao2 + random.randint(-30,30)
        self.speed = self.speed + random.randint(-15,15)
        self.Km_Sign = self.Km_Sign + self.speed*self.Timing
        Send_Data = self.Gen_Send_Xml()
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

    def Gen_Send_Xml(self):
        myXMLGenerator = Gen.XMLGenerator()
        #XML Root Node
        MyLadarScanner = myXMLGenerator.createNode("MyLadarScanner")
        myXMLGenerator.setNodeAttr(MyLadarScanner,"From","Linux Server")
        myXMLGenerator.addNode(node = MyLadarScanner)

        #book01
        Measured_Data = myXMLGenerator.createNode("Measured_Data")

        lachu1 = myXMLGenerator.createNode("lachu1")
        myXMLGenerator.setNodeValue(lachu1,str(self.lachu1))
        myXMLGenerator.addNode(lachu1,Measured_Data)

        lachu2 = myXMLGenerator.createNode("lachu2")
        myXMLGenerator.setNodeValue(lachu2,str(self.lachu2))
        myXMLGenerator.addNode(lachu2,Measured_Data)

        daogao1 = myXMLGenerator.createNode("daogao1")
        myXMLGenerator.setNodeValue(daogao1,str(self.daogao1))
        myXMLGenerator.addNode(daogao1,Measured_Data)

        daogao2 = myXMLGenerator.createNode("daogao2")
        myXMLGenerator.setNodeValue(daogao2,str(self.daogao2))
        myXMLGenerator.addNode(daogao2,Measured_Data)

        speed = myXMLGenerator.createNode("speed")
        myXMLGenerator.setNodeValue(speed,str("%.2f"%self.speed))
        myXMLGenerator.addNode(speed,Measured_Data)

        Km_Sign = myXMLGenerator.createNode("Km_Sign")
        myXMLGenerator.setNodeValue(Km_Sign,str("%.2f"%self.Km_Sign))
        myXMLGenerator.addNode(Km_Sign,Measured_Data)

        myXMLGenerator.addNode(Measured_Data, MyLadarScanner)  
        
        return myXMLGenerator.genXml()

if __name__ == '__main__':

    My = MyLadarScanner()

    My.Start_Listening(10021)
   
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
        print(My.Rec_Str)
        My.Send_Socket_Data("Server side is ready")



        t = threading.Thread(target = My.Check_Recv_Str,args=(1024,))
        t.start()
        while My.Recv_Sign == 0:
            pass
        My.Recv_Sign = 0
        if My.Rec_Str == '':
            My.Stop_Listening()
            continue
        Xml_Str = My.Rec_Str

        if My.Sep_Initial_Data(Xml_Str) == 1 :
            print(My.Height)
            print(My.Km_Sign)
            print(My.Timing)
            print(My.Dis_Start)
            print(My.Dis_End)
            print(My.Cur_Start)
            print(My.Cur_End)
            My.Send_Socket_Data("Success")
        else:
            print("ERROR")
        

        t = threading.Thread(target = My.Check_Recv_Str,args=(1024,))
        t.start()
        while My.Recv_Sign == 0:
            My.Send_All_Data()
            time.sleep(My.Timing)

        My.Recv_Sign = 0
        if My.Rec_Str == '':
            My.Stop_Listening()
            continue
        print(My.Rec_Str)


        My.Stop_Listening()







