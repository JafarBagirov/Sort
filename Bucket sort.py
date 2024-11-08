# bucket sort
# verilənləri müxtəlif aralıklara bölərək hər aralığı ayrıca sıralayır 

lst = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]

# Bucket sayını təyin et (adətən siyahının uzunluğuna bərabər seçilir)
n = len(lst)
buckets = [[] for _ in range(n)]

# Elementləri vedrələrə yerləşdir
for x in lst:
    index = int(x * n)  # Vedrənin indeksini hesablayırıq
    buckets[index].append(x)

# Hər vedrədəki elementləri sıralayıb əsas siyahıya əlavə et
sorted_lst = []
for bucket in buckets:
    # Vedrədəki elementləri sıralayırıq (burada sadəcə sort() funksiyasından istifadə olunur)
    for x in sorted(bucket):
        sorted_lst.append(x)

print(sorted_lst)
