#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 00:40:22 2018

@author: dandelion
"""

# =============================================================================
# from numpy import *
#
# ma=mat(random.rand(4,4))
# ma_re=ma.I
# print('ma source matrix is:\n',ma)
# print('ma reverse matrix is:\n',ma_re)
# print('ma*ma_re=:\n',ma*ma_re)
# print('')
# =============================================================================

import pandas as pd
import numpy as np

# =============================================================================
# 1. Series
# 定义：数据表中的一列或一行，观测向量为一维数组，对于任意一组个体某一属性的观测可抽象为Series的概念。
#Series默认由index和values构成。
#
# =============================================================================
np.random.seed(1)     #使用随机种子，这样每次运行random结果一致，
A=np.random.randn(5)
print("A is an array:\n",A)
S = pd.Series(A)
print("S is a Series:\n",S)
print("index: ", S.index)  #默认创建索引，注意是从0开始
print("values: ", S.values)

np.random.seed(2)
s=pd.Series(np.random.randn(5),index=['a','b','c','d','e'])
print (s)
print("Index of the Series :\n",s.index)

stocks={'中国平安':'601318','格力电器':'000651','招商银行':'600036',
        '中信证券':'600030','贵州茅台':'600519'}
Series_stocks = pd.Series(stocks)
#Series_stocks.index.name='股票名称'
print (Series_stocks)

# =============================================================================
# 1.2 Series数据的访问
# =============================================================================

print("取出第0、1行数据:\n",Series_stocks[:2])
print("取出第1,4,2行数据:\n",Series_stocks[[1,4,2]])
print("取出中国平安、中信证券数据:\n",Series_stocks[['中国平安','中信证券']])

# =============================================================================
# 根据索引返回已排序的新对象：
# Series.sort_index(ascending=True)
# 根据值返回已排序的对象，NaN值在末尾：
# Series.sort_values(ascending=True)
# 为各组分配一个平均排名：
# Series.rank(method='average',ascending=True,axis=0)
# rank的method选项：
# 'average'：在相等分组中，为各个值分配平均排名
# 'max','min'：使用整个分组中的最小排名
# 'first'：按值在原始数据中出现的顺序排名
# 返回含有最大值的索引位置：
# Series.idxmax()
# 返回含有最小值的索引位置：
# Series.idxmin()
# =============================================================================
#1.3 Series排序函数
index_sorted_series=Series_stocks.sort_index(ascending=True)
print ("index_sorted_series:\n",index_sorted_series)

value_sorted_series=Series_stocks.sort_values(ascending=True)
print("value_sorted_series:\n",value_sorted_series)

#每个数的平均排名
Rank_Series_stocks=Series_stocks.rank(method='average',ascending=True,axis=0)
print("Rank_Series_stocks:\n",Rank_Series_stocks)


#返回含有最大值的索引位置：
print(s.idxmax())

#返回含有最小值的索引位置：
print(s.idxmin())

# =============================================================================
# 2 Pandas数据结构：DataFrame
# DataFrame是一个二维的数据结构，通过数据组，index和columns构成
#DataFrame是多个Series的集合体。
# =============================================================================
#通过字典创建DataFrame
d={'one':pd.Series([1.,2.,3.],index=['a','b','c']),
   'two':pd.Series([1.,2.,3.,4.,],index=['a','b','c','d']),
   'three':range(4),
   'four':1.,
   'five':'f'}
df=pd.DataFrame(d)
print (df)

#可以使用dataframe.index和dataframe.columns来查看DataFrame的行和列，
#dataframe.values则以数组的形式返回DataFrame的元素
print ("DataFrame index:\n",df.index)
print ("DataFrame columns:\n",df.columns)
print ("DataFrame values:\n",df.values)

#DataFrame也可以从值是数组的字典创建，但是各个数组的长度需要相同：
d = {'one': [1., 2., 3., 4.], 'two': [4., 3., 2., 1.]}
df = pd.DataFrame(d, index=['a', 'b', 'c', 'd'])
print(df)

#另一种创建DataFrame的方法十分有用，那就是使用concat函数基于Series
#或者DataFrame创建一个DataFrame
a = pd.Series(range(5))   #range(5)产生0到4
b = pd.Series(np.linspace(4, 20, 5)) #linspace(a,b,c)
df = pd.concat([a, b], axis=1)
print (df)
# =============================================================================
# 其中的axis=1表示按列进行合并，axis=0表示按行合并，
# 并且，Series都处理成一列，所以这里如果选axis=0的话，
# 将得到一个10×1的DataFrame。
# =============================================================================

# =============================================================================
# 2.2 DataFrame数据的访问
# =============================================================================
#DataFrame是以列作为操作的基础的，全部操作都想象成先从DataFrame里取一列，
#再从这个Series取元素即可。
#可以用datafrae.column_name选取列，也可以使用dataframe[]操作选取列

f = pd.DataFrame()
index = ['alpha', 'beta', 'gamma', 'delta', 'eta']
for i in range(5):
    a = pd.DataFrame([np.linspace(i, 5*i, 5)], index=[index[i]])
    df = pd.concat([df, a], axis=0)
print('df: \n',df)
print ("df[1]:\n",df[1])
df.columns = ['a', 'b', 'c', 'd', 'e']
print('df: \n',df)
print ("df[b]:\n",df['b'])
print ("df.b:\n",df.b)
print ("df[['a','b']]:\n",df[['a', 'd']])

#访问特定的元素可以如Series一样使用下标或者是索引:
print (df['b'][2])       #第b列，第3行（从0开始算）
print (df['b']['gamma']) #第b列，gamma对应行
##### df.loc['列或行名']，df.iloc[n]第n行，df.iloc[:,n]第n列

#若需要选取行，可以使用dataframe.iloc按下标选取，
#或者使用dataframe.loc按索引选取
print (df.iloc[1])    #选取第一行元素
print (df.loc['beta'])#选取beta对应行元素

#选取行还可以使用切片的方式或者是布尔类型的向量：
print ("切片取数:\n",df[1:3])
#行列组合起来选取数据：
print (df[['b', 'd']].iloc[[1, 3]])
print (df.iloc[[1, 3]][['b', 'd']])
print (df[['b', 'd']].loc[['beta', 'delta']])
print (df.loc[['beta', 'delta']][['b', 'd']])
#如果不是需要访问特定行列，而只是某个特殊位置的元素的话，
#dataframe.at和dataframe.iat
#是最快的方式，它们分别用于使用索引和下标进行访问
print(df)
print (df.iat[2, 3])  #相当于第3行第4列
print (df.at['gamma', 'd'])


# =============================================================================
# 2.3创建时间序列
#pandas.date_range(start=None, end=None, periods=None, freq='D',
#tz=None, normalize=False, name=None, closed=None, **kwargs)
# =============================================================================
dates_by_Day=pd.date_range('20180101',periods=12,freq='D')
dates_by_Month=pd.date_range('20180101',periods=12,freq='M')
dates_by_Year=pd.date_range('20180101',periods=12,freq='Y')
print("dates_by_Day\n",dates_by_Day)
print("dates_by_Month\n",dates_by_Month)
print("dates_by_Year\n",dates_by_Year)

#查看数据头n行 ,默认n=5
print(df.head())
#查看数据最后3行
print(df.tail(3))

#查看数据的index(索引）,columns （列名）和数据
print("index of df:\n",df.index)
print("columns of df:\n",df.columns)
print("values of df:\n",df.values)
#数据转置
# df.T

#根据索引排序数据排序：（按行axis=0或列axis=1）

df.sort_index(axis=1,ascending=False)

#按某列的值排序
df.sort_values(['a'])  #按A列的值从小到大排序

df.loc['20180131':'20180430',['a','c']]  #根据标签取数

df.iloc[1:3,1:4]  #根据所在位置取数，注意从0开始数

df.iloc[[1,3,5],[0,3]]  #根据特定行和列取数

df[df.A>0] #相当于取出A列大于0时的数据列表

df[df>0]  #显示值大于0的数，其余使用NaN代替

#数据筛选isin()

df2=df.copy() #复制df数据
df2['E']=np.arange(12)
df2


df2[df2['E'].isin([0,2,4])]

# =============================================================================
# 3. 缺失值处理
# =============================================================================

#缺失值用NaN显示

date3=pd.date_range('20181001',periods=5)
np.random.seed(6)
data=np.random.randn(5,4)
df3=pd.DataFrame(data,index=date3,columns=list('ABCD'))
print(df3)

df3.iat[3,3]=np.NaN  #令第3行第3列的数为缺失值（0.129151）
df3.iat[1,2]=np.NaN  #令第1行第2列的数为缺失值（1.127064）
print(df3)
#丢弃存在缺失值的行
#设定how=all只会删除那些全是NaN的行：
df3.dropna(how='any')

#删除列也一样，设置axis=1
df3.dropna(how='any',axis=1)
#thresh参数,如thresh=4,一行中至少有4个非NaN值，否则删除
df3.iloc[2,2]=np.NaN
df3.dropna(thresh=4)


# =============================================================================
# 填充缺失值
# fillna 还可以使用 method 参数
# method 可以使用下面的方法
# 1 . pad/ffill：用前一个非缺失值去填充该缺失值
# 2 . backfill/bfill：用下一个非缺失值填充该缺失值
# =============================================================================

df3.fillna(method='ffill')


df3.fillna(method='bfill')
print(df3)


#使在改变DataFrame 和 Series 的操作时，会返回一个新的对象，
#原对象不变，如果要改变原对象，可以添加参数 inplace = True用列均值填充
#使用该列的均值填充
df3['C'].fillna(df3['C'].mean(),inplace=True)
print(df3)


# =============================================================================
# 4、统计
# =============================================================================
date4=pd.date_range('20181001',periods=5)
np.random.seed(7)
data4=np.random.randn(5,4)
df4=pd.DataFrame(data4,index=date3,columns=list('ABCD'))
df4
#描述性统计 df.describe()

df4.describe()
df4.mean() #均值，默认按列axis=0
df4.mean(axis=1)  #按行


#对数据使用函数df.apply()

df4.apply(np.cumsum) #np.cumsum()累加函数
df4.apply(lambda x:x.max()-x.min()) #lambda自定义函数
#相当于计算每列里最大值-最小值

df4['E']=['a','a','a','b','b']
#计算某个值出现评率
df4['E'].value_counts()


# =============================================================================
# 5、数据合并
# =============================================================================
#Concat（）
d1=pd.Series(range(5))
print(d1)
d2=pd.Series(range(5,10))
print(d2)
pd.concat([d1,d2],axis=1) #默认是纵向合并即axis=0

#pd.merge(left_on=None, right_on=None, left_index=False,
#right_index=False)
d1=pd.DataFrame(np.random.randn(3,3),columns=list('ABC'))
print(d1)
d2=pd.DataFrame(np.random.randn(3,3),columns=list('DEF'))
print(d2)
pd.merge(d1,d2,left_index=True, right_index=True)


#增加1行数据：Append()
df = pd.DataFrame(np.random.randn(3, 3), columns=['A','B','C'])
df

s=pd.Series([1.,1,1],index=list('ABC'))
df.append(s,ignore_index=True)

# =============================================================================
# 聚类分析 groupby
# =============================================================================
df = pd.DataFrame({'A' : ['true', 'false', 'true', 'false',
                           'true', 'false', 'true', 'false'],
                    'B' : ['one', 'one', 'two', 'three',
                          'two', 'two', 'one', 'three'],
                    'C' : np.random.randn(8),
                    'D' : np.random.randn(8)})
df
df.groupby(['A']).sum()  #以A列特征分类并加总
df.groupby(['A','B']).sum()

# =============================================================================
# 数据透视表
# =============================================================================

df = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,
                   'B' : ['A', 'B', 'C'] * 4,
                   'C' : ['foo', 'foo', 'foo', 'bar', 'bar',
                          'bar'] * 2,
                   'D' : np.random.randn(12),
                   'E' : np.random.randn(12)})
df


pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])


# =============================================================================
# 6、数据可视化（画图）
# =============================================================================
import matplotlib.pyplot as plt
#from pylab import mpl
#mpl.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
#mpl.rcParams['axes.unicode_minus']=False  # 用来正常显示负号


#ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000',
#                periods=1000))
#ts = ts.cumsum()
#ts.plot(figsize=(12,8))

#利用tushare包抓取股票数据并画图
#得到的是DataFrame的数据结构
import tushare as ts
df=ts.get_k_data('sh',start='1990-01-01')
import pandas as pd
df.index=pd.to_datetime(df['date'])
df['close'].plot(figsize=(12,8))
plt.title("sh trending")

# =============================================================================
# df=ts.get_gdp_year()
# df=ts.get_gdp_year()
# df.index=df['year']
# df['gdp'].plot(figsize=(12,6))
# plt.title("gdp trending")
# =============================================================================
