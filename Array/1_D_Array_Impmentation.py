array = [10, 3, 7, 5]
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
max = array[0]

for num in array:
    if num > max:
        max = num

print(max)
min = array[0]

for num in array:
    if num < max:
        min = num

print(min)
