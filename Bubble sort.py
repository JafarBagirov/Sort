# bubble sort
# ardıcıl cütlər şəkilində müqayisə edərək sıralayır
A=[6,4,2,5,3,1]
n=len(A)
for i in range(n-1):
    for j in range(n-1-i):
        if A[j]>A[j+1]:
            A[j],A[j+1]=A[j+1],A[j]
print(A)



