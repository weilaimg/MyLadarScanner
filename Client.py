import XMLGenerator as Gen
from socket import *


def Generator_Xml_Str():
    myXMLGenerator = Gen.XMLGenerator()

    #XML Root Node
    MyLadarScanner = myXMLGenerator.createNode("MyLadarScanner")
    myXMLGenerator.setNodeAttr(MyLadarScanner,"From","Android Client")
    myXMLGenerator.addNode(node = MyLadarScanner)

    #book01
    Initial_Data = myXMLGenerator.createNode("Initial_Data")

    Height = myXMLGenerator.createNode("Height")
    myXMLGenerator.setNodeValue(Height,"40")
    myXMLGenerator.addNode(Height,Initial_Data)

    Km_Sign = myXMLGenerator.createNode("Km_Sign")
    myXMLGenerator.setNodeValue(Km_Sign,"0")
    myXMLGenerator.addNode(Km_Sign,Initial_Data)

    Timing = myXMLGenerator.createNode("Timing")
    myXMLGenerator.setNodeValue(Timing,"200")
    myXMLGenerator.addNode(Timing,Initial_Data)

    Dis_Start = myXMLGenerator.createNode("Dis_Start")
    myXMLGenerator.setNodeValue(Dis_Start,"2.0")
    myXMLGenerator.addNode(Dis_Start,Initial_Data)

    Dis_End = myXMLGenerator.createNode("Dis_End")
    myXMLGenerator.setNodeValue(Dis_End,"4.0")
    myXMLGenerator.addNode(Dis_End,Initial_Data)

    Cur_Start = myXMLGenerator.createNode("Cur_Start")
    myXMLGenerator.setNodeValue(Cur_Start,"60")
    myXMLGenerator.addNode(Cur_Start,Initial_Data)

    Cur_End = myXMLGenerator.createNode("Cur_End")
    myXMLGenerator.setNodeValue(Cur_End,"120")
    myXMLGenerator.addNode(Cur_End,Initial_Data)


    myXMLGenerator.addNode(Initial_Data, MyLadarScanner)  
    
    return myXMLGenerator.genXml()

if __name__ == "__main__":
    
    serverName = '127.0.0.1'
    serverPort = 10021
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    i = input("Please input I :")
    clientSocket.send(bytes(i,encoding="utf8"))

    print(str(clientSocket.recv(1024),encoding="utf8"))

    sentence = Generator_Xml_Str()

    clientSocket.send(bytes(sentence,encoding="utf8"))

    print(str(clientSocket.recv(1024),encoding="utf8"))
    
    while 1:
        str1 = clientSocket.recv(1024)
        print(str(str1,encoding="utf8"))
    

    i = input("Please input I :")
    clientSocket.send(bytes(i,encoding="utf8"))

    print(str(clientSocket.recv(1024),encoding="utf8"))
    #clientSocket.send(bytes('asd',encoding="utf8"))
    

    clientSocket.close()
    
