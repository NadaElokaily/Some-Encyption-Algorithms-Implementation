import copy
size = int(input())
permutation = []
permutation = input().split(" ")

inversePermutation = ["A" for j in range(size)]


SortedList= copy.copy(permutation)
SortedList= [int(x) for x in SortedList]
'''SortedList.sort()
print (SortedList)
'''
s1=set(SortedList)
#print("S1")
#print(s1)
s2 = set()
k=1
while k <= size:
    s2.add(k)
    k+=1

#print("S2")
#print(s2)


counter=1

if(set(s1)!=set(s2)):
    print("IMPOSSIBLE")


else:
    for i in permutation:
        inversePermutation[int(i)-1]= counter
        counter +=1
    print (' '.join(str(v) for v in inversePermutation))
