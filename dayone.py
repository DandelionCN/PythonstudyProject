from collections import deque
q=deque()
q.append('welcome to the sea')
print(q)
q.append(345)
print(q)
print('-----this is a seperate line ----------')


import heapq
nums=[1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# print(nums.sort())
print('The largest n number is:',heapq.nlargest(3,nums))
print('the smallest n number is:',heapq.nsmallest(4,nums))
print('the sorted sequene is:',heapq.nlargest(len(nums),nums))
print('the sorted sequene is:',heapq.nsmallest(len(nums),nums))

print('-----this is another seperate line ----------')
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap=heapq.nsmallest(3,portfolio,key=lambda s:s['price'])
expensive=heapq.nlargest(3,portfolio,key=lambda s:s['price'])
print('All the elemnts are as this:',portfolio)
print('The cheapest three are:',cheap)
print('The most expensive three are:',expensive)

heap=[1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.heapify(heap)
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heap)
print(sorted(heap)[:3])
print(sorted(heap)[-3:])