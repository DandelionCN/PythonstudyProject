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
import datetime


def Pdf_Cdf_Create_Function(Input_kpidata_array_or_series):
# ================================
#     parameter:Input_kpidata_array_or_series
#     parameter datatype:array or array_liked pandas.series
#     import matplotlib.pyplot as plt is needed
#     import numpy as np is needed
#     import os is needed
# ================================
    global kpi_title
    figure=plt.figure(num=None, figsize=(6.4,4.8), dpi=100, facecolor='w', edgecolor='b')
    #figsize must be less than 2^16 inches in each direction.the default figsize=(6.4, 4.8)

    pdf_ax1=figure.add_subplot()

    hist, bin_edges = np.histogram(Input_kpidata_array_or_series,bins=100,)
    #PDF图创建
    width = (bin_edges[1] - bin_edges[0]) * 1.0
    pdf_ax1.bar(bin_edges[1:], hist/sum(hist), align='center',width=width,bottom=None,color="b",edgecolor='b',linewidth=None,tick_label=None)
    #color='#5B9BD5'or 'b','c','m','r','y','k','w','g'

    #x轴坐标刻度及标签设置
    pdf_ax1.set_xlim([bin_edges.min(), bin_edges.max()])
    xlabel=np.linspace(bin_edges.min(),bin_edges.max()-0.0001,11,endpoint=True)
#    pdf_ax1.set_xticklabels(xlabel,fontsize=8)
    pdf_ax1.set_xticks(xlabel,minor=False)
    pdf_ax1.set_xlabel(kpi_title)

    #y1轴坐标刻度及标签设置
    pdf_ax1.set_ylim([0, round(max(hist)/sum(hist),2)])
    y1label=np.linspace(0,round(max(hist)/sum(hist),2),6,endpoint=True)
    pdf_ax1.set_yticks(y1label)
    pdf_ax1.set_ylabel("PDF")

    #设置网格线
    pdf_ax1.grid(b=True,axis='both',linestyle='--')

    #CDF图创建
    cdf_ax2=pdf_ax1.twinx()
    cdf = np.cumsum(hist/sum(hist))
    cdf_ax2.plot(bin_edges[1:], cdf, linestyle='-', color='#ED7D31',linewidth=3,marker=None,markersize=None)


    #y2轴坐标刻度及标签设置
    cdf_ax2.set_ylim([0, 1.0])
    y2label=np.linspace(0,1.0,11,endpoint=True)
    cdf_ax2.set_yticks(y2label)
    cdf_ax2.set_ylabel("CDF")

    #图表标题设置

    plt.title("CDF & PDF of "+ kpi_title,fontsize=10)
#    plt.legend(title=kpi_title,loc='best',fontsize=8)

    #保存生成的图标为制定格式的图片
#    figure=plt.gcf()
    date_cur=datetime.datetime.now().strftime("%Y%m%d%H%m")
    figname_full = os.path.join(os.getcwd(),"CDF_PDF_Figure_"+ kpi_title +"_"+date_cur+".png")
    figure.savefig(figname_full,transparent=True)
#    figure.savefig(figname_full,dpi=200,facecolor='w', edgecolor='w',papertype=None, format='png',transparent=False)
    #显示图片
    plt.show()
#    return hist, bin_edges

#def Scatter(dataframe):


if __name__=="__main__":
    csv_log="DTlog_coverage.csv"
    file_fullname=os.path.join(os.getcwd(),csv_log)
    tuelog=pd.read_csv(file_fullname,sep=",",header=0,index_col=False)
    tuelog=tuelog.replace('--','NaN').fillna(method='ffill')
    columns=dict(enumerate(tuelog.columns))
    print("Columns list is:\n",columns)
    while True:
        try:
            select_index=int(input("Please input the column index number to make CDF&PDF:\n"))
            print("The Selected KPI is:",columns[select_index])
            kpi_title=columns[select_index]
            break
        except:
            print("The input is invalid,try again!")
            print("The columns list is:\n",columns)
    print("the Figure is coming on....")
    tuelog=tuelog.dropna(subset=[kpi_title])
#    tuelog=tuelog.loc[(tuelog[kpi_title]!=0)]
    kpi_arr=tuelog[kpi_title]
    Pdf_Cdf_Create_Function(kpi_arr)
#    hist, bin_edges=Pdf_Cdf_Create_Function(kpi_arr)



