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

# II method non rekursiv _______________________________________
arr = [38, 27, 43, 3, 9, 82, 10, -8, -89, -56, -75, 46, 443, 4, 3, 4, 3, 4, 95, 6, 11654, 612, 64, 6]

n = len(arr)
hisse = 1
while hisse < n:
    for left_sratr in range(0, n, hisse*2):
        mid = min(left_sratr+hisse-1, n-1)
        right_end = min(left_sratr + hisse*2-1, n-1)
        n1 = mid-left_sratr+1
        n2 = right_end - mid
        L = arr[left_sratr:left_sratr+n1]
        R = arr[mid+1:mid+1+n2]
        i=j=0
        k = left_sratr



        while i < n1 and j < n2:
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < n1:
            arr[k] = L[i] 
            i += 1
            k += 1
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
    hisse *= 2
print(arr)

