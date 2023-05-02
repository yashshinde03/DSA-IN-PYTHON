arr = [10, 3, 7, 5]
# print(array)
# Random Indexing
# print(array[2])
# to get all items
# print(array[:])
# to get item specific number
# print(array[1:2])
# to get last 2 items
# print(array[:-1])
# Linear Search
max = arr[0]

for num in arr:
    if num > max:
        max = num

print(max)
min = arr[0]

for num in arr:
    if num < max:
        min = num

print(min)
