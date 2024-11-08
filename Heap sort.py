# heap Sort
# yığın strukturu istifadə edərək sıralama aparır. ən böyük və ən kiçik elementləri çıxarır

lst = [38, 27, 43, 3, 9, 82, 10]

# Siyahının uzunluğunu tapırıq
n = len(lst)

# Yığı (heap) qurmaq
i = n // 2 - 1  # İlk qeyri-yarpağı tapırıq
while i >= 0:
    parent = i
    while 2 * parent + 1 < n:
        # Sol və sağ uşaqları tapırıq
        child = 2 * parent + 1
        if child + 1 < n and lst[child] < lst[child + 1]:
            child += 1
        # Əgər valideyn ən böyük deyilsə, dəyişdir
        if lst[parent] < lst[child]:
            lst[parent], lst[child] = lst[child], lst[parent]
            parent = child
        else:
            break
    i -= 1

# Yığdan çıxararaq sırayla sıralamaq
j = n - 1
while j > 0:
    # Max element ilə son elementi dəyiş
    lst[0], lst[j] = lst[j], lst[0]
    # Yığını yenidən düzəlt
    parent = 0
    while 2 * parent + 1 < j:
        child = 2 * parent + 1
        if child + 1 < j and lst[child] < lst[child + 1]:
            child += 1
        if lst[parent] < lst[child]:
            lst[parent], lst[child] = lst[child], lst[parent]
            parent = child
        else:
            break
    j -= 1

print(lst)