# merge sort
# siyahını iki hissəyə ayıraraq hər hissəni ayrı sıralayır və birləşdirir 

lst = [38, 27, 43, 3, 9, 82, 10]
while len(lst) > 1:
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    merged = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged += left[i:]
    merged += right[j:]
    
    lst = merged
print(lst)
