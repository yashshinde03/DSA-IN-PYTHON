def find_duplicates(nums):
    for num in nums:
     if nums[abs(num)] >= 0:
         nums[abs(num)] = -nums[abs(num)]
     else:
         print('Repetition : %s' % str(abs(num)))


n = [2, 1, 3, 2, 3]
find_duplicates(n)