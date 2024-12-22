# counting sort
# Bu algoritm yalnız müsbət tam ədədləri və aralıqları məhdud olan ədədləri sıralamaq üçün effektivdir

lst = [4, 2, 2, 8, 3, 3, 1]

# Siyahıdakı ən böyük elementi tapırıq
max_value = max(lst)

# Sayma siyahısını (count array) qururuq
count = [0] * (max_value + 1)

# Hər elementin sayını tapırıq
for num in lst:
    count[num] += 1

# Sıralanmış siyahını yaradaraq doldururuq
sorted_lst = []
for i in range(len(count)):
    sorted_lst.extend([i] * count[i])  # Hər elementi sayına uyğun əlavə edirik

print(sorted_lst)

# counting sort alqoritmi II method ________________________________________________________________________

A=[2,2,6,1,6,2,2]
maks=max(A)
say=[0]*(maks+1)
for i in range(len(A)):
    say[A[i]]+=1

"""
say=[0,0,0,0,0,0,0]
say[2]=1
say[2]=2
say[6]=1
say[1]=1
say[6]=2
say[2]=3
say[2]=4
--------------------------------------------
     0 1 2 3 4 5 6   -> elementleri
say=[0,1,4,0,0,0,2]  -> elementlerin saylari
"""

for i in range(1,maks+1):
    say[i]+=say[i-1]
"""
0,1,4,0,0,0,2
--------------
  1,4,0,0,0,2
--------------
  1,5,0,0,0,2
--------------
  1,5,5,0,0,2
--------------
  1,5,5,5,0,2
--------------
  1,5,5,5,5,2
--------------
  1,5,5,5,5,7
"""

B=[0]*len(A)
for i in range(len(A)-1,-1,-1):
    B[say[A[i]]-1] = A[i]
    say[A[i]]-=1
"""
----------------------
say[1]=1 -> 0
say[2]=5 -> 4, 3, 2, 1
say[6]=7 -> 6, 5 
2 ->  B[4]=2
2 ->  B[3]=2
6 ->  B[6]=6
1 ->  B[0]=1
6 ->  B[5]=6
2 ->  B[2]=2
2 ->  B[1]=2
B=[1,2,2,2,2,6,6]
-----------------------
"""

A=B
print(A)
