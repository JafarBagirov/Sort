# Map Sort misalı
def map_sort(data):
    # Verilənləri key-value cütləri ilə sıralayırıq
    sorted_map = dict(sorted(data.items()))
    return sorted_map

# Məsələn input: key-value cütləri
data = {
    'apple': 4,
    'banana': 2,
    'cherry': 7,
    'date': 1
}

sorted_data = map_sort(data)
print("Sıralanmış Map:", sorted_data)
