# selection sort
# ən kiçik və ya ən böyük elementləri seçərək sıralanmış hissəyə əlavə edir
A=[6,4,2,5,3,1]
n=len(A)
for i in range(n):
    print(A)
    mini=A[i]
    mini_ind=i
    for j in range(i+1,n):
        if A[j]<mini:
            mini=A[j]
            mini_ind=j
    A[i],A[mini_ind]=A[mini_ind],A[i]