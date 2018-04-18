
#####----获取最大或最小的N个元素---------------------------

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

#####----使用多个界定符分割字符串---------------------------
#当你使用 re.split() 函数时候，需要特别注意的是正则表达式中是否包含一个括号捕获分组。
# 如果使用了捕获分组，那么被匹配的文本也将出现在结果列表中。
# Notice the difference betwean the '[]'and '()' 正则表达式
#ues the '[]' 代表可选项，或关系，，分隔符好直接罗列即可；
#ues the '（）' 分割符之间需要使用‘|’，进行分割；
line = 'asdf fjdk; afed, fjek,asdf, foo'
line2 = 'sdfh, shdi_etfdgf;sdf   follshe'
import re
fields=re.split(r'[;,\s]\s*',line)
print(fields)

fields2 = re.split(r'(;|,|\s)\s*', line)
print(fields2)

split_test=re.split(r'[,;\s_]\s*',line2)
print(split_test)
split_test2=re.split(r'(,|;|\s|_)\s*',line2)
print(split_test2)

##2.2 字符串开头或结尾匹配
#检查字符串开头或结尾的一个简单方法是使用 str.startswith() 或者是 str.endswith() 方法。
#如果你想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去， 然后传给 startswith() 或者 endswith() 方法：
filename='http://www.python.org'
start=filename.startswith('http')
end=filename.endswith('.org')
print(start)
print(end)

#如果你想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去， 然后传给 startswith() 或者 endswith() 方法：
import os
paths=''
filenames=os.listdir('.')
print(filenames)

# for name in filenames:
#     if name.endswith(('.c', '.h')):
#         print(name)
#     else:pass

from urllib.request import urlopen
def read_data(strname):
    if strname.startswith(('http','https','ftp')):
        return urlopen(strname).read()
    else:
        with open(strname) as f:
            return f.read()


url='http://python3-cookbook.readthedocs.io/zh_CN/latest/c02/p02_match_text_at_start_end.html'
print(read_data(url))

