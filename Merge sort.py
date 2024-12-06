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

lst = [5, 8, 9, 1, 3, 5, 6, 2, 55, 66, 222, 3, 25, 6, 15, 3, 344, 92, 315, 15, 23, 9]
sorted_lst = merge_sort(lst)
print(sorted_lst)