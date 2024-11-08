# radix sort
# rəqəmlərin basamak dəyərlərinə görə  sıralama aparır

lst = [170, 45, 75, 90, 802, 24, 2, 66]

# Ən böyük elementi tap
max_num = max(lst)

# Hər rəqəm səviyyəsində sıralama
exp = 1
while max_num // exp > 0:
    # Sayma sıralaması (counting sort) üzrə mövcud `exp` üçün
    output = [0] * len(lst)
    count = [0] * 10

    # Hər rəqəmin sayını say
    for i in range(len(lst)):
        index = (lst[i] // exp) % 10
        count[index] += 1

    # Sayları kumulyativ şəkildə artır
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Output siyahısını doldur
    i = len(lst) - 1
    while i >= 0:
        index = (lst[i] // exp) % 10
        output[count[index] - 1] = lst[i]
        count[index] -= 1
        i -= 1

    # Nəticəni `lst`-ə köçür
    for i in range(len(lst)):
        lst[i] = output[i]

    # Növbəti rəqəm səviyyəsinə keç
    exp *= 10

print(lst)