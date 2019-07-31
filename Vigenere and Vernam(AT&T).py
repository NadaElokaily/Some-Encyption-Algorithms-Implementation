Key= input()
Plain= input()
VigenereCipher=""
VernamCipher=""
OneTimePad="YES"
ExtendedKey=Key

i=0
while (len(ExtendedKey)) < (len(Plain)):
    OneTimePad="NO"
    ExtendedKey=ExtendedKey+Key[i]
    i=i+1
    if i>=(len(Key)):
       i=0
#print (ExtendedKey)

k=0
for j in Plain:
    Ascii=ord(j)-65+ ord(ExtendedKey[k])
    if Ascii > 90:
        VigenereCipher=VigenereCipher+(chr(Ascii-26))
    else:
        VigenereCipher=VigenereCipher+(chr(Ascii))
    k=k+1

k=0
for c in Plain:
    AsciiPlain=ord(c)
    AsciiKey =ord(ExtendedKey[k])
    VernamCipherBuffer =(AsciiPlain ^ AsciiKey)
    VernamCipher=VernamCipher+ str('{:02X}'.format(VernamCipherBuffer))
    k=k+1




print('Vigenere: %s' %VigenereCipher)
print('Vernam: %s' %VernamCipher)
print('One-Time Pad: %s' %OneTimePad)

'''
TEST
CORRECT
'''
