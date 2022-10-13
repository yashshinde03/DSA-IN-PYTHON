import heapq
nums = [4 ,7 , 3, -2, 1, 0]
heap = []
for value in nums:
    heapq.heappush(heap,value)

while heapq:
    print(heapq.heappop(heap))
