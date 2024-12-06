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
