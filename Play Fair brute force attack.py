from itertools import permutations
def ExistsInMatrix(c):
    row=0
    col=0
    for row in range(3):
        for col in range(3):
            if Matrix[row][col]== c:
                return 1;
    return 0

def GetRow(c):
    row=0
    col=0
    for row in range(3):
        for col in range(3):
            if Matrix[row][col]== c:
                return row
def GetCol(c):
    row=0
    col=0
    for row in range(3):
        for col in range(3):
            if Matrix[row][col]== c:
                return col
'''
def CreateBruteforcekey():
    PossibleCharacters = "ABCDEFGHI"
    Bruteforcekey = []
    Prms = (p for p in permutations(PossibleCharacters))
    for p in Prms:
        print(p)
        Bruteforcekey.append(''.join(p))
    return  Bruteforcekey'''

def CreateBruteforcekey():
    PossibleCharacters = "ABCDEFGHI"
    Prms = (p for p in permutations(PossibleCharacters))
    for p in Prms:
        if(MixCol(InitialPlain,''.join(p))==InitialCipher):
            print(''.join(p))
            break


def CreateMatrix(key):    
    Matrix= [['a']*3 for j in range (3)]
    col=0
    row=0
    i=0
    for row in range(3):
        for col in range(3):
            Matrix[row][col]=key[i]
            i=i+1
    return(Matrix)

def MixCol(Plain,bfk1):
    Matrix=CreateMatrix(bfk1)
    Cipher=[]
    p=0
    for p in range(0,len(Plain),2):
        '''
        PRow=GetRow(Plain[p])
        PCol=GetCol(Plain[p])
        IPRow=GetRow(Plain[p+1])
        IPCol=GetCol(Plain[p+1])
        '''
        PRow = 0
        PCol = 0
        IPRow = 0
        IPCol = 0
        for r in range(3):
            for c in range(3):
                if Matrix[r][c] == Plain[p]:
                    PRow = r
                    PCol = c
                if Matrix[r][c] == Plain[p+1]:
                    IPRow = r
                    IPCol = c
      
        if PRow == IPRow:
            Cipher.append(Matrix[PRow][(PCol+1)%3])
            Cipher.append( Matrix[IPRow][(IPCol+1)%3])
            
        elif PCol == IPCol:
            Cipher.append(Matrix[(PRow+1)%3][PCol])
            Cipher.append(Matrix[(IPRow+1)%3][IPCol])

        else:
            Cipher.append(Matrix[PRow][IPCol])
            Cipher.append(Matrix[IPRow][PCol])
    CP="".join(Cipher)
    return CP

i=0
j=0
InitialPlain=input()
InitialCipher=input()

CreateBruteforcekey()
'''
Bruteforcekeys = CreateBruteforcekey()
for bfk in Bruteforcekeys:
    if(MixCol(InitialPlain,bfk)==InitialCipher):
        print(bfk)
        break'''
        

'''
ICED
CFFE
'''


