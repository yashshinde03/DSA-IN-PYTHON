def reverseInteger(n):
    reversed = 0
    remainder = 0
    while n > 0:
        remainder = int(n % 10)
        n = int(n/10)
        reversed = reversed * 10 + remainder
    print(reversed)

reverseInteger(1234)

