# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 16:36:16 2018

@author: admin
"""
import pandas as pd
import os

def make_uelog_result_savedir(sourcedata_path):
    uelog_result_savedir = os.path.join(sourcedata_path, "Result")
    pathisExists = os.path.exists(uelog_result_savedir)
    if not pathisExists:
        os.mkdir(os.path.join(sourcedata_path, "Result"))
        print("已新建结果数据保存路径为：\n{}".format(uelog_result_savedir))
    else:
        print("结果数据保存路径已经存在，路径为：\n{}".format(uelog_result_savedir))
    return uelog_result_savedir




#file_path=r"D:\system study\py\testlog\ue1KPILog20180731110133.csv"
file_path=(input('Please input the source file with full name:\n')).strip()[1:-1]



df_data=pd.read_csv(file_path,sep=',',header=0)
#cols=df_data.columns.values
#print(cols)
#字段计算公式制定
df_data['CSIrsrp_Average']=df_data.apply(lambda x:(x['CSIRsrp_1']+x['CSIRsrp_2']+x['CSIRsrp_3']+x['CSIRsrp_4'])/4,axis=1)

df_data['CSISinr_Average']=df_data.apply(lambda x:(x['CSISinr_1']+x['CSISinr_2']+x['CSISinr_3']+x['CSISinr_4'])/4,axis=1)

df_data['SSBlockSinr_Average']=df_data.apply(lambda x:(x['SSBlockSinr_1']+x['SSBlockSinr_2']+x['SSBlockSinr_3']+x['SSBlockSinr_4'])/4,axis=1)

df_data['ULThroughput_Total']=df_data.apply(lambda x:(x['ULThroughput_1']+x['ULThroughput_2'])/1024,axis=1)

df_data['DLThroughput_Total']=df_data.apply(lambda x:(x['DLThroughput_1']+x['DLThroughput_2']+x['DLThroughput_3']+x['DLThroughput_4'])/1024,axis=1)

df_data['NCell1SSBRsrp_Average']=df_data.apply(lambda x:(x['NCell1SSBRsrp_1']+x['NCell1SSBRsrp_2']+x['NCell1SSBRsrp_3']+x['NCell1SSBRsrp_4']+x['NCell1SSBRsrp_5']+x['NCell1SSBRsrp_6']+x['NCell1SSBRsrp_7']+x['NCell1SSBRsrp_8'])/8,axis=1)

df_data['NCell2SSBRsrp_Average']=df_data.apply(lambda x:(x['NCell2SSBRsrp_1']+x['NCell2SSBRsrp_2']+x['NCell2SSBRsrp_3']+x['NCell2SSBRsrp_4']+x['NCell2SSBRsrp_5']+x['NCell2SSBRsrp_6']+x['NCell2SSBRsrp_7']+x['NCell2SSBRsrp_8'])/8,axis=1)

df_data['ULMcs_Average']=df_data.apply(lambda x:(x['ULMcs_1']+x['ULMcs_2'])/2,axis=1)

df_data['PuschBler_Average']=df_data.apply(lambda x:(x['PuschBler_1']+x['PuschBler_2'])/2,axis=1)

df_data['DLMcs_Average']=df_data.apply(lambda x:(x['DLMcs_1']+x['DLMcs_2']+x['DLMcs_3']+x['DLMcs_4'])/2,axis=1)

df_data['PdschBler_Average']=df_data.apply(lambda x:(x['PdschBler_1']+x['PdschBler_2']+x['PdschBler_3']+x['PdschBler_4'])/4,axis=1)

#需求字段提取及输出
#output_data=df_data[['Time','GPSTime','GPSLong','GPSLA','GPSHeigh','Ue Id','Pci','ULRbNum','TxPwr','CRNTI','DLRbNum','MIMOMod','CQI','PbchCrcErrorNum','PbchCrcSuccNum','PbchCrcSucc_Scale','OptimalAvgRSRP','CSIrsrp_Average','CSISinr_Average','SSBlockSinr_Average','ULMcs_Average','PuschBler_Average','ULThroughput_Total','DLMcs_Average','PdschBler_Average','DLThroughput_Total','NCell1Pci','NCell1SSBRsrp_Average'
#,'NCell2Pci','NCell2SSBRsrp_Average']]

#output_data=df_data[['Time','GPSTime','GPSLong','GPSLA','CSIrsrp_Average','CSISinr_Average','SSBlockSinr_Average','ULThroughput_Total','DLThroughput_Total','Ue Id','Pci','ULRbNum','TxPwr','CRNTI','DLRbNum','MIMOMod','CQI','PbchCrcErrorNum','PbchCrcSuccNum','PbchCrcSucc_Scale','OptimalAvgRSRP','ULMcs_Average','PuschBler_Average','DLMcs_Average','PdschBler_Average','NCell1Pci','NCell1SSBRsrp_Average','NCell2Pci','NCell2SSBRsrp_Average','GPSHeigh']]

output_data=df_data[['Time','Ue Id','GPSLong','GPSLA','CSIrsrp_Average','CSISinr_Average','SSBlockSinr_Average','ULThroughput_Total','DLThroughput_Total','Pci','ULRbNum','CRNTI','DLRbNum','MIMOMod','CQI','PbchCrcErrorNum','PbchCrcSuccNum','PbchCrcSucc_Scale','OptimalAvgRSRP','ULMcs_Average','PuschBler_Average','DLMcs_Average','PdschBler_Average','NCell1Pci','NCell1SSBRsrp_Average','NCell2Pci','NCell2SSBRsrp_Average','GPSHeigh']]


print(output_data.head(3))
save_path=make_uelog_result_savedir(os.path.dirname(file_path))
savefile_fullname=os.path.join(save_path,(os.path.basename(file_path)[:-4])+'_Result.csv')
output_data.to_csv(savefile_fullname,sep=',',header=True,index=False)

#pandas for date analysis

from datetime import timedelta
from pandas import DataFrame
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

path = 'links_date.csv'

# Open original data
parse_dates = ['start', 'end']
df = pd.read_csv(path, index_col='tmdbId', parse_dates=parse_dates)

# Drop null data
df.dropna(inplace=True)

# Fill null data
# df.fillna(0, inplace=True)

# Obtain hourly data
df['DELTATIME'] = df['end'] - df['start']

# Select column
df = df[df['DELTATIME'] == timedelta(hours=1)]

# Drop column
df.drop('DELTATIME', axis=1, inplace=True)

# Handle data

#用Numpy来实现直方图频数统计的
np.histogram() 默认地使用10个相同大小的区间（箱），然后返回一个元组（频数，分箱的边界），如上所示。要注意的是：这个边界的数量是要比分箱数多一个的.
hist, bin_edges = np.histogram(arr)

#Matplotlib基于Numpy的histogram进行了多样化的封装并提供了更加完善的可视化功能。
n, bins, patches = plt.hist(x=arr, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('My Very Own Histogram')


#使用Pandas的 Series.histogram() ，并通过 matplotlib.pyplot.hist() 来绘制输入Series的直方图
import pandas as pd

size, scale = 1000, 10
commutes = pd.Series(np.random.gamma(scale, size=size) ** 1.5)

commutes.plot.hist(grid=True, bins=20, rwidth=0.9,
                   color='#607c8e')
#array.plot.hist(grid=True, bins=20, rwidth=0.9,
                   color='#607c8e')
plt.title('Commute Times for 1,000 Commuters')
plt.xlabel('Counts')
plt.ylabel('Commute Time')
plt.grid(axis='y', alpha=0.75)
plt.show()


#一个更高级可视化工具就是Seaborn，它是在matplotlib的基础上进一步封装的强大工具。对于直方图而言，Seaborn有 distplot() 方法，可以将单变量分布的直方图和kde同时绘制出来，
import seaborn as sns

sns.set_style('darkgrid')
sns.distplot(d)
#distplot方法默认的会绘制kde，并且该方法提供了 fit 参数，可以根据数据的实际情况自行选择一个特殊的分布来对应。

sns.distplot(d, fit=stats.laplace, kde=False)




#pandas也提供了一个方便的.value_counts() 方法，用来计算一个非空值的直方图，并将之转变成一个pandas的series结构，示例如下：
import pandas as pd

>>> data = np.random.choice(np.arange(10), size=10000,
...                         p=np.linspace(1, 11, 10) / 60)
>>> s = pd.Series(data)

>>> s.value_counts()
s.value_counts(normalize=True).head()
#此外，pandas.cut() 也同样是一个方便的方法，用来将数据进行强制的分箱。比如说，我们有一些人的年龄数据，并想把这些数据按年龄段进行分类，示例如下：

>>> ages = pd.Series(
...     [1, 1, 3, 5, 8, 10, 12, 15, 18, 18, 19, 20, 25, 30, 40, 51, 52])
>>> bins = (0, 10, 13, 18, 21, np.inf)  # 边界
>>> labels = ('child', 'preteen', 'teen', 'military_age', 'adult')
>>> groups = pd.cut(ages, bins=bins, labels=labels)

>>> groups.value_counts()
child           6
adult           5
teen            3
military_age    2
preteen         1
dtype: int64

>>> pd.concat((ages, groups), axis=1).rename(columns={0: 'age', 1: 'group'})
