a,b,c= map(int,input().split(' '))
b= bin(b)[2:]

Pwr = 1
Total = 1
counter =0
for i in reversed(b):
    Pwr = Pwr * Pwr
    Pwr = Pwr % c
    if counter == 0:
        Pwr = a
    if i == '1':
        Total = Total*Pwr
        Total = Total %c
    counter= counter+1
print (Total)
        
