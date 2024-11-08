# insertion sort
# hər elementi sıralanmış siyahıya daxil edərək sıralayır
A=[6,4,2,5,3,1]
n=len(A)
for i in range(1,n):
    j=i
    print(A)
    while j>0 and A[j]<A[j-1]:
        A[j],A[j-1]=A[j-1],A[j]
        j-=1
        print(A)
    print("----------------")