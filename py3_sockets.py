import socket

sk = socket.socket()
sk.connect(("115.159.31.137",12000))

sk.sendall(bytes("ab",encoding="utf8"))

i=0

while i<4850:
    a = str(sk.recv(1), encoding="utf8")
    print(a,end='')
    i=i+1
print('\n')

sk.close()
