#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 22:09:45 2020

@author: dandelion
"""

import pandas as pd

file=r"/home/dandelion/Desktop/log.csv"

data=pd.read_csv(file,header=0,sep=",")

#区间门限
bins=[-150,-110,-100,-90,-80,-70,-30]

#各区间的标签
label=labels=["(-150,-110]","(-110,-100]","(-100,-90]","(-90,-80]","(-80,-70]","(-70,-30]"]

#分区间操作
data["rsrp_range"]=pd.cut(data["OptimalAvgRSRP"],bins=bins,labels=label,right=True)

#新增字段查看
columns=data.columns.to_list()
print("数据表头字段清单为:\n",columns)
print("----------------------------")

#使用聚合 groupby方式统计各区域采样点数
pdf=data.groupby(data["rsrp_range"]).agg({"rsrp_range":"count"})
#导出区间统计结果
pdf.to_csv("各区间采样点数by(groupby).csv")
print("各区间采样点数by(groupby):\n",pdf)

print("---------------------")

#使用pd.value_counts()方式统计各区间的采样点数
value_count=pd.value_counts(data["rsrp_range"],sort=False)
print("各区间采样点数by(value_counts()):\n",value_count)

"""
#代码执行结果示例:
#--------------------
各区间采样点数:
              rsrp_range
rsrp_range
(-150,-110]         253
(-110,-100]          14
(-100,-90]          186
(-90,-80]            73
(-80,-70]             0
(-70,-30]             0
---------------------
各区间采样点数:
 (-150,-110]    253
(-110,-100]     14
(-100,-90]     186
(-90,-80]       73
(-80,-70]        0
(-70,-30]        0
Name: rsrp_range, dtype: int64
"""