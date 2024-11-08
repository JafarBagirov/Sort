"""
Sieve of Eratosthenes
n=20
2 -> 4 6 8 10 12 14 16 18 20
3 -> 9 12 15 18
4 -> 
-----------------------------
2 3 5 7 11 13 17 19
"""
n=int(input())
sade=[1]*(n+1)
sade[0]=0
sade[1]=0
i=2
while i*i<=n:
    j=i*i
    if sade [i] == 1:
        while j<=n:
            sade[j]=0
            j+=i
        i+=1

for i in range(n+1):
    if sade[i]==1:
        print(i,end=" ")