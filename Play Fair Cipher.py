def ExistsInMatrix(c):
    row=0
    col=0
    for row in range(5):
        for col in range(5):
            if Matrix[row][col]== c:
                return 1;
    return 0

def GetRow(c):
    for row in range(5):
        for col in range(5):
            if Matrix[row][col]== c:
                return row
def GetCol(c):
    row=0
    col=0
    for row in range(5):
        for col in range(5):
            if Matrix[row][col]== c:
                return col



InitialKey=input()
veryInitialPlain=input()
InitialPlain=''
Key=''
mm=0
for mm in range(len(veryInitialPlain)):    
    if (veryInitialPlain[mm]=='J'):
        InitialPlain+='I'
    else:
        InitialPlain+=veryInitialPlain[mm]

for mm in range(len(InitialKey)):    
    if (InitialKey[mm]=='J'):
        Key+='I'
    else:
        Key+=InitialKey[mm]
        
#print(InitialPlain)

Plain=''


counter = 0
while counter < len(InitialPlain):
    if counter != (len(InitialPlain)-1):    
        if (InitialPlain[counter] == InitialPlain[counter+1]) :
            if (InitialPlain[counter]!='X'):
                Plain= Plain + InitialPlain[counter]
                Plain= Plain+ 'X'
                counter=counter+1
            else:
                Plain= Plain + InitialPlain[counter]
                Plain= Plain+ 'Q'
                counter=counter+1
            
        else:
            Plain= Plain + InitialPlain[counter]
            Plain= Plain + InitialPlain[counter+1]
            counter=counter+2
    else:
        Plain= Plain + InitialPlain[counter]
        counter= counter+1
        if (divmod(len(Plain),2)[1]==1) and (Plain[len(Plain)-1]!= 'X'):
            Plain= Plain+'X'
        elif (divmod(len(Plain),2)[1]==1) and (Plain[len(Plain)-1]== 'X'):
            Plain = Plain+ 'Q'
#print(Plain)
        


Cipher=''

Matrix= [['a' for i in range(5)] for j in range (5) ]

RowCounter=0
ColCounter=0

for k in Key:
    if ExistsInMatrix(k)==1:
        continue
    else:
        Matrix[RowCounter][ColCounter]=k
        ColCounter=ColCounter+1
        if(ColCounter >= 5):
            ColCounter=0            
            RowCounter=RowCounter+1
#print (Matrix)

o=65
while o <= 90:
    if chr(o)!= 'J':
        if ExistsInMatrix(chr(o))!= 1:
            Matrix[RowCounter][ColCounter]=chr(o)
            #print (Matrix[RowCounter][ColCounter])
            ColCounter=ColCounter+1
            if(ColCounter >= 5):
                ColCounter=0            
                RowCounter=RowCounter+1
    o=o+1

#print (Matrix)
p=0
while p < len(Plain):
        if GetRow(Plain[p])== GetRow(Plain[p+1]):
            Cipher+= Matrix[GetRow(Plain[p])][divmod((GetCol(Plain[p])+1),5)[1]]
            Cipher+= Matrix[GetRow(Plain[p+1])][divmod((GetCol(Plain[p+1])+1),5)[1]]
            
        elif GetCol(Plain[p])==GetCol(Plain[p+1]):
            Cipher+= Matrix[divmod((GetRow(Plain[p])+1),5)[1]][GetCol(Plain[p])]
            Cipher+= Matrix[divmod((GetRow(Plain[p+1])+1),5)[1]][GetCol(Plain[p+1])]

        else:
            Cipher+= Matrix[GetRow(Plain[p])][GetCol(Plain[p+1])]
            Cipher+= Matrix[GetRow(Plain[p+1])][GetCol(Plain[p])]
        p=p+2
        

print(Cipher)

