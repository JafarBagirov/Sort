# merge sort
# siyahını iki hissəyə ayıraraq hər hissəni ayrı sıralayır və birləşdirir 

def merge_sort(lst):
    if len(lst) <= 1:
        return lst  # Əsas hal: tək elementli siyahı artıq sıralıdır.

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])  # Sol hissəni rekursiv sırala.
    right = merge_sort(lst[mid:])  # Sağ hissəni rekursiv sırala.

    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Qalan elementləri əlavə et
    merged += left[i:]
    merged += right[j:]
    return merged

lst = [38, 27, 43, 3, 9, 82, 10]
sorted_lst = merge_sort(lst)
print(sorted_lst)
