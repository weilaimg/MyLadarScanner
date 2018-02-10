def Hex_To_Dec(dhex):
    dec = 0
    i=0
    while dhex[i]!='\0':
        print(dhex[i],end='')
        i = i+1
    i=0
    while dhex[i]!='\0':
        if (dhex[i]>='0' and dhex[i]<='9'):
            dec = dec*16+int(dhex[i])
        if(dhex[i]>='A' and dhex[i]<='F'):
            dec = dec*16+int(ord(dhex[i])-ord('A')+10)
        i=i+1
    return dec

if __name__ == "__main__":
    dhex = [0,1,2,3,4]
    dhex[0] = 'B'
    dhex[1] = 'C'
    dhex[2] = 'D'
    dhex[3] = '\0'
    dhex[4] = 'D'
    dec = Hex_To_Dec(dhex)
    print (dec)