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