import math

sizePermutation = int(input())
permutation = []
permutation = input().split(" ")
sizePlain = int(input())
plain = input()

#plain = int(plain,16)

TEST =str('{:04b}'.format(int(plain,16)).zfill(sizePlain))
#buffer =[0 for i in range (sizePlain)]
buffer=''

j=0
for j in range(sizePermutation):
    X= int(permutation[j])-1
    buffer += TEST[X]

#buffer= "".join(buffer)
buffer= int(buffer,2)

HexOutput= '{:X}'.format((buffer))

print(HexOutput)
