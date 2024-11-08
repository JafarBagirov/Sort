# binary search
# massiv ortadan ikiyə bölünür. axtarılan element orta elementlə müqayisə edilir.

lst = [3, 9, 10, 27, 38, 43, 66, 75, 82, 90]
target = 43

# İndeksləri təyin edirik
left = 0
right = len(lst) - 1
found = False

# Binary Search
while left <= right:
    mid = (left + right) // 2  # Orta indeksi tapırıq
    if lst[mid] == target:
        found = True
        break
    elif lst[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

if found:
    print(f"{target} siyahıda mövcuddur.")
else:
    print(f"{target} siyahıda yoxdur.")