import math
MatrixLength=int(math.sqrt(int(input())))

KeyBuffer=input().split()
Key=[[0 for x in range(MatrixLength)] for y in range(MatrixLength)]
k=0
for i in range(MatrixLength):
    for j in range(MatrixLength):
             Key[i][j]= int(KeyBuffer[k])
             k=k+1
#print (Key)

PlainBuffer=[[0]for y in range(MatrixLength)]
result=[[0]for y in range(MatrixLength)]
FullResult=[]

Plain=input()
while divmod(len(Plain),MatrixLength)[1] > 0:
    Plain= Plain+'X'
#print(Plain)

size =int(len(Plain)/MatrixLength)
#print(size)
L=0
j=0
i=0
while i < size:
        #print(L)
        result=[[0]for y in range(MatrixLength)]
        for j in range(MatrixLength):
                PlainBuffer[j][0]=ord(Plain[L])-65
                #print(chr(PlainBuffer[j][0]+65))
                L=L+1
                M=0
                N=0
                O=0
                
        for M in range(len(Key)):
                for N in range(len(PlainBuffer[0])):
                    for O in range(len(PlainBuffer)):
                        result[M][N] += Key[M][O] * PlainBuffer[O][N]
        #print('tt')
        #print(chr(divmod(result[0][0],26)[1]+65))
        for r in range (len(result)):
            result[r]=divmod(result[r][0],26)[1]
            #print (chr(result[r]+65))
            FullResult.append(chr(result[r]+65))
        
        i=i+1
        
print("".join(FullResult))
        
        

'''
4
7 8 11 11
SHORT
'''
