def quick_sort(arr):
    # Əgər massivdə 1 və ya daha az element varsa, artıq sıralıdır
    if len(arr) <= 1:
        return arr
    else:
        # Pivot seçirik (bu nümunədə sonuncu elementi pivot olaraq götürürük)
        pivot = arr[-1]
        left = [x for x in arr[:-1] if x <= pivot]  # Pivotdan kiçik və bərabər olan elementlər
        right = [x for x in arr[:-1] if x > pivot]   # Pivotdan böyük olan elementlər
        
        # Sol və sağ tərəfləri təkrarlayaraq sıralama prosesini bitiririk
        return quick_sort(left) + [pivot] + quick_sort(right)

# Nümunə üçün massiv
arr = [12, 4, 7, 9, 3, 5, 6, 2, 8, 1]
sorted_arr = quick_sort(arr)
print("Sıralanmış massiv:", sorted_arr)


# rekursiv olmadan ________________________________________________________________________________

arr = [38, 27, 43, 3, 9, 82, 10, -8, -89, -56, -75, 46, 443, 4, 3, 4, 3, 4, 95, 6, 11654, 612, 64, 6]

stack = [(0, len(arr)-1)]
while stack:
    start, end = stack.pop()
    if start >= end:
        continue
    pivot = arr[(start+end)//2]
    left, right = start, end
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    if start < right:
        stack.append((start, right))
    if left < end:
        stack.append((left, end))
print(arr)
