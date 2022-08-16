import timeit
str1 = "race"
str2 = "races"


def checkAnagram(subject, anagram):
    if sorted(subject) == sorted(anagram):
        print("Anagram")
    else:
        print("Not an Anagram")

result = timeit.timeit(stmt='checkAnagram(str1, str2)', globals=globals(), number=4)
print(f"Execution time is {result / 4} seconds")

