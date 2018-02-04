import serial

ser = serial.Serial('/dev/rfcomm0', 9600, timeout=1)
t = ser.read(20)
while t == bytes('',encoding="utf8"):
    t = ser.read(20)

print(t)
i = 1
while i<100:
    ser.write(bytes("fuck you man",encoding="utf8"))
    i=i+1
ser.close()
