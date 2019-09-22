#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:03:00 2019

@author: dandelion
测试数据CSV文件需要与当前程序路径相同
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


def Pdf_Cdf_Create_Function(Input_kpidata_array_or_series):
# ================================
#     parameter:Input_kpidata_array_or_series
#     parameter datatype:array or array_liked pandas.series
#     import matplotlib.pyplot as plt is needed
#     import numpy as np is needed
#     import os is needed
# ================================
    hist, bin_edges = np.histogram(kpi_arr,bins=100,)
    #PDF图创建
    width = (bin_edges[1] - bin_edges[0]) * 1.0
    plt.bar(bin_edges[1:], hist/max(hist), align='center',width=width,bottom=None,color="b",edgecolor='b',linewidth=None,tick_label=None)
    #color='#5B9BD5'or 'b','c','m','r','y','k','w','g'
    #CDF图创建
    cdf = np.cumsum(hist/sum(hist))
    plt.plot(bin_edges[1:], cdf, linestyle='-', color='#ED7D31',linewidth=3,marker=None,markersize=None)
    #x轴坐标刻度及标签设置
    plt.xlim([bin_edges.min(), bin_edges.max()])
    xlabel=np.linspace(bin_edges.min(),bin_edges.max()-0.0001,11,endpoint=True)
    plt.xticks(xlabel,fontsize=8)
    #y轴坐标刻度及标签设置
    plt.ylim([0, 1.0])
    ylabel=np.linspace(0,1.0,11,endpoint=True)
    plt.yticks(ylabel,fontsize=8)
    #图表标题设置
    plt.title(' CDF & PDF By '+'Input_kpidata',fontsize=8)
    #plt.legend(title='Input_kpidata',loc='best',fontsize=8)
    plt.grid(b=True)
    plt.show()


if __name__=="__main__":
    csv_log="ue1KPILog20190303170052.csv"
    file_fullname=os.path.join(os.getcwd(),csv_log)
    tuelog=pd.read_csv(file_fullname,sep=",",header=0,index_col=False)
    tuelog=tuelog.replace('--','NaN').fillna(method='ffill')

    kpi_arr=tuelog["NR_OptimalAvgRsrp"]
    Pdf_Cdf_Create_Function(kpi_arr)


