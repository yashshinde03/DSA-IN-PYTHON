array = [1, 2, 3, 4, 5, 6]


def reverseArray(arr):
    start_index = 0
    end_index = len(arr) - 1
    while start_index < end_index:
        # swapping the array element
        arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
        start_index += 1
        end_index -= 1
    print(arr)


reverseArray(array)
