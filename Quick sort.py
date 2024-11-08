# quick sort
# pivot seçir və elementləri pivota görə kiçik və böyük qruplara ayırır

lst = [38, 27, 43, 3, 9, 82, 10]

stack = [lst]
sorted_list = []
while stack:
    sublist = stack.pop()

    if len(sublist) <= 1:
        sorted_list += sublist
        continue

    pivot = sublist[0]
    less = [x for x in sublist[1:] if x <= pivot]
    greater = [x for x in sublist[1:] if x > pivot]

    stack.append(greater)
    stack.append([pivot])
    stack.append(less)

print(sorted_list)