def Mul2 (X):
    X=int (X)
    result = X << 1
    if result > 0xFF:
        result = result ^ 0x11B
    result = "{:02x}".format(result).zfill(2)
    return result
    

N1 ,N2  = input().split(' ')
N1 = int(N1,16)
N2 = int(N2,16)

Addition = "{:02X}".format(N1 ^ N2).zfill(2)
Multiplication = 0x00
Temp = int(N1)
i=0
while i<8:
    if (i==0):
        Temp =int(N1)
    else:
        Temp = int(Mul2(Temp),16)
    if (N2 & (1<<i)):
        Multiplication = Multiplication ^ Temp
    i=i+1
Multiplication = "{:02X}".format(Multiplication).zfill(2)

print (Addition,Multiplication)

