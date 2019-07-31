'''
Input
The input consists of 1 line that has 2 numbers M, N respectively

Output
In case N has no multiplicative inverse, print "IMPOSSIBLE" without the quotes.
Otherwise print 2 numbers which represent the additive and multiplicative inverses respectively of N.
All printed numbers must be mod(M)
'''
def AddInv(M,N):
    if N==0:
        AddInverse=0
    elif N > 0:
        AddInverse= M-N      
    return AddInverse


M ,N  = input().split(' ')
M=int(M)
N=int(N)
while (N < 0):
    N= M+N
while (N > M):
    N= N-M
A1,A2,A3= 1,0,M
B1,B2,B3= 0,1,N

while 1:
    if B3==0:
        print("IMPOSSIBLE")
        break
    if B3==1:
        if B2 <0:
            B2 = M+B2
        print("%s %s" % (AddInv(M,N),B2))
        break
    Q = A3//B3
    T1,T2,T3 = A1-Q*B1 , A2-Q*B2 , A3-Q*B3
    A1,A2,A3 = B1,B2,B3
    B1,B2,B3 = T1,T2,T3
    
