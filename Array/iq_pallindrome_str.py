import timeit
str = "abba"


def palindromeCheck(str):
    global flag
    start_index = 0
    end_index = len(str) - 1
    while start_index < end_index:
        # swapping the array element
        if str[start_index] == str[end_index]:
            flag = 1
        else:
            flag = 0
            break
        start_index += 1
        end_index -= 1
    if flag == 1:
        print("It is a Palindrome")
    else:
        print("Not a palindrome")

# Checking execution time
# result = timeit.timeit(stmt='palindromeCheck(str)', globals=globals(), number=4)
# print(f"Execution time is {result / 4} seconds")

