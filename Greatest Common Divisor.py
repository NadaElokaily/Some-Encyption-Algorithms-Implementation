var1 ,var2  = input().split(' ')
if var1>var2:
    First = int(var1)
    Second = int(var2)
else:
    First = int(var2)
    Second = int(var1)
while (Second >0):
    Temp = Second
    Second = First % Second
    First = Temp

        
print (First)
