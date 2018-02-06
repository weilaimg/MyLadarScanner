from socket import *
import threading 
import time 
import xml.dom.minidom

class MyLadarScanner:
    def Start_Listening(self):
        Server_Port = 10022
        self.serverSocket = socket(AF_INET,SOCK_STREAM)
        self.serverSocket.bind(('',Server_Port))
        self.serverSocket.listen()
        self.Recv_Sign = 0
        print ('The server is ready to receive')

    def Get_Socket_Connect(self):
        self.connectionSocket, self.addr = self.serverSocket.accept()
        self.serverSocket.setblocking(True)

    def Get_Recv_Str(self,rwnd):
        Rec_Str = self.connectionSocket.recv(rwnd)
        return str(Rec_Str,encoding="utf8")

    def Check_Recv_Str(self,rwnd):
        Rec_Str = self.connectionSocket.recv(rwnd)
        self.Rec_Str = str(Rec_Str,encoding="utf8")
        self.Recv_Sign = 1

    def Send_Socket_Data(self,Send_Data):
        self.connectionSocket.send(bytes(Send_Data,encoding="utf8"))

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
            Height = Initial_Data.getElementsByTagName("Height")[0].childNodes[0].data
            Km_Sign = Initial_Data.getElementsByTagName("Km_Sign")[0].childNodes[0].data
            Timing = Initial_Data.getElementsByTagName("Timing")[0].childNodes[0].data
            Dis_Start = Initial_Data.getElementsByTagName("Dis_Start")[0].childNodes[0].data
            Dis_End = Initial_Data.getElementsByTagName("Dis_End")[0].childNodes[0].data
            Cur_Start = Initial_Data.getElementsByTagName("Cur_Start")[0].childNodes[0].data
            Cur_End = Initial_Data.getElementsByTagName("Cur_End")[0].childNodes[0].data
            flag = 1
            self.Set_Init_Data(Height,Km_Sign,Timing,Dis_Start,Dis_End,Cur_Start,Cur_End)
        except:
            flag = 0

        return flag

    def Stop_Listening(self):
        self.serverSocket.close()




if __name__ == '__main__':

    My = MyLadarScanner()

    My.Start_Listening()
    My.Get_Socket_Connect()

    t = threading.Thread(target = My.Check_Recv_Str,args=(1024,))
    t.start()
    while My.Recv_Sign == 0:
        pass
    My.Recv_Sign = 0

    Xml_Str = My.Rec_Str

    if My.Sep_Initial_Data(Xml_Str) == 1 :
        print("Height=%s"%My.Height)
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
        pass
    My.Recv_Sign = 0

    print(My.Rec_Str)


    My.Stop_Listening()







