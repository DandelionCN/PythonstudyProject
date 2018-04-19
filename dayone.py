
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
def read_data(name):
    if name.startswith(('http:','https:','ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


url='http://python3-cookbook.readthedocs.io/zh_CN/latest/c02/p02_match_text_at_start_end.html'
print(read_data(url))

#使用正则表达式实现匹配
import re
re.match('http:|https:|ftp:',url)
print(re.match('http:|https:|ftp:',url))

#字符串搜索和替换
#对于简单的字面模式，直接使用 str.replace() 方法即可
text = 'yeah, but no, but yeah, but no, but yeah'
print(text)
print(text.replace('yeah','yep'))

#对于复杂的模式，请使用 re 模块中的 sub() 函数。 为了说明这个，假设你想将形式为 11/27/2012 的日期字符串改成 2012-11-27 。
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(text)
import re
print(re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',text))

#删除字符串中不需要的字符
#strip() 方法能用于删除开始或结尾的字符。 lstrip() 和 rstrip() 分别从左和从右执行删除操作。
#  默认情况下，这些方法会去除空白字符，但是你也可以指定其他字符。比如：
s = ' hello world! \n'
print('origenal string s is :',s)
print('striped string s is:',s.strip())
print('Left striped string s is:',s.lstrip())
print('Right striped string s is:',s.rstrip())


s2 = 'hello      world! \n'
import re
print(re.sub(r'\s+',' ',s2))

#通常情况下你想将字符串 strip 操作和其他迭代操作相结合，比如从文件中读取多行数据。 如果是这样的话，那么生成器表达式就可以大显身手了。
with open(r'C:\Users\admin\Desktop\记录.txt') as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)

s3='------------hell world===============  '
print((s3.strip()).strip('-='))
print((s3.strip()).strip('='))


#format()函数用于字符串格式化对齐
#函数 format() 同样可以用来很容易的对齐字符串。 你要做的就是使用 <,> 或者 ^ 字符后面紧跟一个指定的宽度
text='hell world!'
print(format(text,'>15'))
print(format(text,'<15'))
print(format(text,'^15'))


#2.14 合并拼接字符串
#join() function
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print('*'.join(parts))


#以指定列宽格式化字符串,使用textwrap.fill()函数对字符串按指定长度进行分割；

import textwrap
text_test='113.3445679'
print(textwrap.fill(text_test,5))
