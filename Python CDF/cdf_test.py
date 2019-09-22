#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 15:30:55 2018

@author: admin """

#from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import plotly_express as px


#import pysnooper as ps

#import seaborn as sns

#load the csv_tuelog to dataframe

#tuelog_file_path=r"/home/dandelion/文档/python/Python test/ue1KPILog20190303170052.csv"

csv_log="ue1KPILog20190303170052.csv"
file_fullname=os.path.join(os.getcwd(),csv_log)

#tuelog_file_path=r"/home/dandelion/文档/python/Python test/ue1KPILog20190303171849.csv"

#tuelog=pd.read_csv(open(tuelog_file_path),sep=",",header=0)
use_columns=['Time','NR_PCI', 'NR_DlFreq', 'NR_UlFreq', 'NR_BandWidth', 'NR_MeaObjNum', 'NR_CellId', 'NR_gNBId', 'GPSTime', 'GPSLongitude', 'GPSLatitude', 'GPSHeigh','NR_OptimalAvgRsrp','NR_OptimalAvgSinr','NR_OptimalAvgRsrq','NR_OptimalAvgRssi', 'NR_UL_MCS_1','NR_PUSCH_BLER_1(%)','NR_UL_Rate_PHY_1','NR_UL_Rate_PDCP_MCG', 'NR_UL_Rate_PDCP_SCG','NR_CQIValue_1','NR_UL_RI', 'NR_DL_RB', 'NR_PDSCH_BLER_1(%)','NR_DL_RI','NR_DLStreamNumTotal','NR_DL_Rate_PHY_1','NR_DL_Rate_PDCP_SCG', 'NR_DL_Rate_PDCP_MCG', 'NR_CSI_RS_Single_TB0_CQI','NR_CSI_RS_Single_RSRP_Rx1', 'NR_CSI_RS_Single_RSRP_Rx2', 'NR_CSI_RS_Single_RSRP_Rx3', 'NR_CSI_RS_Single_RSRP_Rx4', 'NR_CSI_RS_Single_SINR_Rx1', 'NR_CSI_RS_Single_SINR_Rx2', 'NR_CSI_RS_Single_SINR_Rx3', 'NR_CSI_RS_Single_SINR_Rx4', 'NR_CSI_RS_Multi_TB0_CQI']

tuelog=pd.read_csv(file_fullname,sep=",",header=0,index_col=False,usecols=use_columns)

tuelog=tuelog.replace('--','NaN').fillna(method='ffill')

tuelog['NR_CSI_RS_Single_RSRP_Rx_avg']=tuelog.apply(lambda x:(float(x['NR_CSI_RS_Single_RSRP_Rx1'])+float(x['NR_CSI_RS_Single_RSRP_Rx2'])+float(x['NR_CSI_RS_Single_RSRP_Rx3'])+float(x['NR_CSI_RS_Single_RSRP_Rx4']))/4, axis=1)

tuelog['NR_CSI_RS_Single_SINR_Rx_avg']=tuelog.apply(lambda x:(float(x['NR_CSI_RS_Single_SINR_Rx1'])+float(x['NR_CSI_RS_Single_SINR_Rx2'])+float(x['NR_CSI_RS_Single_SINR_Rx3'])+float(x['NR_CSI_RS_Single_SINR_Rx4']))/4,axis=1)

real_use_cloumns=['GPSTime', 'Time','NR_gNBId','NR_CellId',  'NR_PCI', 'NR_DlFreq', 'NR_UlFreq', 'NR_BandWidth', 'NR_MeaObjNum', 'GPSLongitude', 'GPSLatitude', 'GPSHeigh','NR_OptimalAvgRsrp','NR_OptimalAvgSinr','NR_OptimalAvgRsrq','NR_OptimalAvgRssi','NR_CSI_RS_Single_RSRP_Rx_avg','NR_CSI_RS_Single_SINR_Rx_avg', 'NR_UL_MCS_1','NR_PUSCH_BLER_1(%)','NR_UL_Rate_PHY_1','NR_UL_Rate_PDCP_MCG', 'NR_UL_Rate_PDCP_SCG','NR_CQIValue_1','NR_UL_RI', 'NR_DL_RB', 'NR_PDSCH_BLER_1(%)','NR_DL_RI','NR_DLStreamNumTotal','NR_DL_Rate_PHY_1','NR_DL_Rate_PDCP_SCG', 'NR_DL_Rate_PDCP_MCG', 'NR_CSI_RS_Single_TB0_CQI', 'NR_CSI_RS_Multi_TB0_CQI']

realuse_data=tuelog[real_use_cloumns]

#=======以上为基础数据处理=========

px.scatter(realuse_data,x='NR_OptimalAvgSinr',y='NR_DL_Rate_PHY_1')
px.ExpressFigure()



#@ps.snoop()
def ticks_label(serial):
    min_data=serial.min()
    max_data=serial.max()
    diff=max_data-min_data
    if diff>1:
#        label=np.linspace(min_data,max_data,int((max_data-min_data)/5))
        label=np.linspace(min_data,max_data,10)
#    else:
#        label=np.linspace(min_data,max_data,int((max_data-min_data)/1.0))
    return label


#tuelog=pd.read_csv(tuelog_file_path,sep=",",header=0,index_col=False,nrows=1).T

#save the columns name
#tuelog.to_csv(r"/home/dandelion/文档/python/Python test/columns.csv",index=True,header=True)
save_dir=os.path.join(os.getcwd(),'result')
save_filename=csv_log[:-4]+"_realdata.csv"
if not os.path.exists(save_dir):
    os.mkdir(save_dir)

realuse_data.to_csv(os.path.join(save_dir,save_filename),index=False,header=True)
#plt.figure()
#realuse_data.plot()
#plt.legend(loc='best')

#"""设置刻度"""
#ax.set_ylim(-3, 3)
#ax.set_yticks([-1,-0.5,0,0.5,1])
#ax.set_xlim([-5, 8])
# ax.set_xticks([-5,5,1])

#设置网格样式
#ax.grid(True, linestyle='-.')

x=realuse_data["Time"]
y1=realuse_data["NR_DL_Rate_PHY_1"]
y2=realuse_data["NR_OptimalAvgSinr"]
plt.scatter(y2,y1)
#lab=np.linspace(-10,40,10)
labx=ticks_label(y2)
laby=ticks_label(y1)
plt.xticks(labx,fontsize=8)
plt.yticks(laby,fontsize=8)


plt.title(' SINR VS NR_DL_Rate_PHY_1',fontsize=8)
plt.xlabel('Sinr',fontsize=8)
plt.ylabel('Throughput',fontsize=8)
plt.legend(loc='best',fontsize=8)


plt.show()

#=============以上为VS散点图=======================





#======CDF/PDF图===============
kpi_arr=realuse_data["NR_OptimalAvgRsrp"]
#kpi_arr=realuse_data["NR_DL_Rate_PHY_1"]/1024
#arr = np.random.normal(size=100)

hist, bin_edges = np.histogram(kpi_arr,bins=100,)

width = (bin_edges[1] - bin_edges[0]) * 1.0
plt.bar(bin_edges[1:], hist/max(hist), align='center',width=width, color='#5B9BD5')

#plt.Line2D(bin_edges[1:], hist/max(hist),linewidth=2,linestyle='--',color='#5B9BD5')

cdf = np.cumsum(hist/sum(hist))
plt.plot(bin_edges[1:], cdf, '-', color='#ED7D31')

plt.xlim([-125, -65])
xlabel=np.linspace(-120,-65,11,endpoint=True)
plt.xticks(xlabel,fontsize=8)

plt.ylim([0, 1.0])
ylabel=np.linspace(0,1.0,11,endpoint=True)
plt.yticks(ylabel,fontsize=8)

plt.title(' CDF & PDF By NR_OptimalAvgRsrp',fontsize=8)
plt.legend(loc='best',fontsize=8)

plt.grid()

#Seaborn有 distplot() 方法，可以将单变量分布的直方图和kde同时绘制出来
#sns.set_style('darkgrid')
#sns.distplot(arr)
#sns.distplot(d, fit=stats.laplace, kde=False)
#sns.distplot(kpi_arr, bins=None, hist=True, kde=True, rug=False, fit=None, hist_kws=None, kde_kws=None, rug_kws=None, fit_kws=None, color=None, vertical=False, norm_hist=False, axlabel=None, label=None, ax=None)

plt.show()




#========

def Pdf_Cdf_Create_Function(Input_kpidata_array_or_series):
#    import matplotlib.pyplot as plt
#    import numpy as np

    hist, bin_edges = np.histogram(kpi_arr,bins=100,)

    #PDF图创建
    width = (bin_edges[1] - bin_edges[0]) * 1.0
    plt.bar(bin_edges[1:], hist/max(hist), align='center',width=width,bottom=None,color="b")
#   color='#5B9BD5'or 'b','c','m','r','y','k','w','g'

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
    plt.title(' CDF & PDF By '+"Input_kpidata",fontsize=8)
    plt.legend(title="Input_kpidata",loc='best',fontsize=8)
    plt.grid(b=True)
    plt.show()



if __name__=="__main__":
    csv_log="ue1KPILog20190303170052.csv"
    file_fullname=os.path.join(os.getcwd(),csv_log)
    use_columns=['Time','NR_PCI', 'NR_DlFreq', 'NR_UlFreq', 'NR_BandWidth', 'NR_MeaObjNum', 'NR_CellId', 'NR_gNBId', 'GPSTime', 'GPSLongitude', 'GPSLatitude', 'GPSHeigh','NR_OptimalAvgRsrp','NR_OptimalAvgSinr','NR_OptimalAvgRsrq','NR_OptimalAvgRssi', 'NR_UL_MCS_1','NR_PUSCH_BLER_1(%)','NR_UL_Rate_PHY_1','NR_UL_Rate_PDCP_MCG', 'NR_UL_Rate_PDCP_SCG','NR_CQIValue_1','NR_UL_RI', 'NR_DL_RB', 'NR_PDSCH_BLER_1(%)','NR_DL_RI','NR_DLStreamNumTotal','NR_DL_Rate_PHY_1','NR_DL_Rate_PDCP_SCG', 'NR_DL_Rate_PDCP_MCG', 'NR_CSI_RS_Single_TB0_CQI','NR_CSI_RS_Single_RSRP_Rx1', 'NR_CSI_RS_Single_RSRP_Rx2', 'NR_CSI_RS_Single_RSRP_Rx3', 'NR_CSI_RS_Single_RSRP_Rx4', 'NR_CSI_RS_Single_SINR_Rx1', 'NR_CSI_RS_Single_SINR_Rx2', 'NR_CSI_RS_Single_SINR_Rx3', 'NR_CSI_RS_Single_SINR_Rx4', 'NR_CSI_RS_Multi_TB0_CQI']
    tuelog=pd.read_csv(file_fullname,sep=",",header=0,index_col=False,usecols=use_columns)
    tuelog=tuelog.replace('--','NaN').fillna(method='ffill')

    tuelog['NR_CSI_RS_Single_RSRP_Rx_avg']=tuelog.apply(lambda x:(float(x['NR_CSI_RS_Single_RSRP_Rx1'])+float(x['NR_CSI_RS_Single_RSRP_Rx2'])+float(x['NR_CSI_RS_Single_RSRP_Rx3'])+float(x['NR_CSI_RS_Single_RSRP_Rx4']))/4, axis=1)

    tuelog['NR_CSI_RS_Single_SINR_Rx_avg']=tuelog.apply(lambda x:(float(x['NR_CSI_RS_Single_SINR_Rx1'])+float(x['NR_CSI_RS_Single_SINR_Rx2'])+float(x['NR_CSI_RS_Single_SINR_Rx3'])+float(x['NR_CSI_RS_Single_SINR_Rx4']))/4,axis=1)

    real_use_cloumns=['GPSTime', 'Time','NR_gNBId','NR_CellId',  'NR_PCI', 'NR_DlFreq', 'NR_UlFreq', 'NR_BandWidth', 'NR_MeaObjNum', 'GPSLongitude', 'GPSLatitude', 'GPSHeigh','NR_OptimalAvgRsrp','NR_OptimalAvgSinr','NR_OptimalAvgRsrq','NR_OptimalAvgRssi','NR_CSI_RS_Single_RSRP_Rx_avg','NR_CSI_RS_Single_SINR_Rx_avg', 'NR_UL_MCS_1','NR_PUSCH_BLER_1(%)','NR_UL_Rate_PHY_1','NR_UL_Rate_PDCP_MCG', 'NR_UL_Rate_PDCP_SCG','NR_CQIValue_1','NR_UL_RI', 'NR_DL_RB', 'NR_PDSCH_BLER_1(%)','NR_DL_RI','NR_DLStreamNumTotal','NR_DL_Rate_PHY_1','NR_DL_Rate_PDCP_SCG', 'NR_DL_Rate_PDCP_MCG', 'NR_CSI_RS_Single_TB0_CQI', 'NR_CSI_RS_Multi_TB0_CQI']

    realuse_data=tuelog[real_use_cloumns]
    kpi_arr=realuse_data["NR_OptimalAvgRsrp"]
    Pdf_Cdf_Create_Function(kpi_arr)





