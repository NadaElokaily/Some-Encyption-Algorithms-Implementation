from collections import deque
def PermutedChoiceOne(plain):
    
    permutation = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4 ]
    sizePlain =64
    TEST =bin(int(plain,16))[2:].zfill(64)
    buffer=''

    j=0
    for j in range(56):
        X= int(permutation[j])-1
        buffer += TEST[X]

    buffer= int(buffer,2)

    HexOutput= '{:X}'.format(buffer).zfill(14)

    return HexOutput

def PermutedChoiceTwo(plain):
    
    permutation=[14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32 ]
    sizePlain =56
    TEST =bin(int(plain,16))[2:].zfill(56)
    buffer=''

    j=0
    for j in range(48):
        X= int(permutation[j])-1
        buffer += TEST[X]

    buffer= int(buffer,2)

    HexOutput= '{:X}'.format(buffer).zfill(12)

    return HexOutput


def Shift (plain,Round):
    
    #print(plain)

    Rotations = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1 ]

    plain= bin(int(plain,16))[2:].zfill(56)
    leftPlain = plain[:28]
    #print(leftPlain)
    rightPlain = plain[28:]     
    #print(rightPlain)


    rot=Rotations[Round]

    ShiftedLeft=leftPlain[rot:]+leftPlain[:rot]
    ShiftedLeft= hex(int(ShiftedLeft,2))[2:].zfill(7)
    #print (ShiftedLeft)

    ShiftedRight= rightPlain[rot:]+rightPlain[:rot]
    ShiftedRight= hex(int(ShiftedRight,2))[2:].zfill(7)
    #print (ShiftedRight)


    Shifted = ShiftedLeft+ShiftedRight
    #print (Shifted)
    return Shifted



PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4 ]

PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32 ]



MasterKey=input()
PC1Output=PermutedChoiceOne(MasterKey)
ShiftOutput = PC1Output

for i in range (16) :
    
    ShiftOutput = Shift (ShiftOutput,i)
    PC2Output= PermutedChoiceTwo(ShiftOutput)
    '''
    if PC2Output != keys2[i]:
        print ('notmatch at round %s' %str(i))
        print (str(keys2[i]))'''
        
    print (PC2Output)




'''
0123456789ABCDEF

keys2 =['0B02679B49A5',
'69A659256A26',
'45D48AB428D2',
'7289D2A58257',
'3CE80317A6C2',
'23251E3C8545',
'6C04950AE4C6',
'5788386CE581',
'C0C9E926B839',
'91E307631D72',
'211F830D893A',
'7130E5455C54',
'91C4D04980FC',
'5443B681DC8D',
'B691050A16B5',
'CA3D03B87032']



00000000FFFFFFFF

keys= ['7B14E93A4B26',
'5998F9164926',
'95E8FA8429D4',
'B66F86E1A2D1',
'7A3F0573860B',
'49B47D1E150E',
'C5C4FE0C71E4',
'F6CBA260E8E1',
'F69B2362E859',
'ABBA47A3951A',
'2976DE8D1722',
'7455F85C4A64',
'D6C97150C8DC',
'8FEB1781B499',
'2F378FAB3621',
'6B178D3B5223']


'''





