#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 18:28:14 2019

@author: dandelion
"""

import os
import xlrd
import pandas as pd
import datetime


def ProjectParameter_create_for_Spark():
    current_path=os.getcwd()
    files_list=os.listdir(current_path)
    #print(files_list)
    file_name=[]
    for files in files_list:
        if ".xls" in files:
            file_name.append(files)
            break

    project_parameter_table_fullname=os.path.join(current_path,file_name[0])
    print("工参表路径及名称为:\n",project_parameter_table_fullname)

    #获取sheetnames
    workbook=xlrd.open_workbook(project_parameter_table_fullname)
    sheetname_list=workbook.sheet_names()
    print("Sheetname清单为:\n",sheetname_list)

    #sheet_data=workbook.sheet_by_name[sheetname_list[0]]

    sheet_data=pd.read_excel(project_parameter_table_fullname,sheet_name=sheetname_list[0],header=0,index_col=None, usecols=None,engine=None)

    #原始工参字段:['区县', '子网', '站点类型', 'CGI', 'SiteName', 'CellName', 'PCI', '中心载频',       'ARFCN', '跟踪区域码', '小区RE参考功率', '管理状态(DU小区配置)', '运行状态(DU小区配置)', '运行状态的详细信息(DU小区配置)', 'Longitude', 'Latitude', '站高', 'Azimuth', '机械下倾角','电子下倾角', '传输口速率', '务IP地址']


    #SKA字段:[SiteId,SiteName,CellName,NR_PCI,Longitude,Latitude,Azimuth,HBWD,Band,ChannelList,CoverageDist,PowerOn,Indoor,DrawAway,CellId,LCellId,VBWD,Height,ETilt,MTilt,RNCId,CI,LAC,TAC,SiteAvgDistNum,PowerOffset,Vendor,Province,City,District,CoverType]
    #Spark字段:Longitude,Latitude,SiteName,CellName,ARFCN,PCI,Azimuth,gNBID,SectorID,CellID,TAC,MechanicalTilt,Height,ElectricalTilt,Indoor,HalfPowerAngle

    CGI_split=sheet_data['CGI'].str.split(pat='-',expand=True)
    CGI_split.columns=['MCC','MNC','gNBID','CellID']
    Final_sheet_data=sheet_data.join(CGI_split)
    Final_sheet_data['SectorID']=Final_sheet_data['CellID']
    Final_sheet_data.rename(columns={'跟踪区域码':'TAC','站高':'Height','电子下倾角':'ElectricalTilt','机械下倾角':'MechanicalTilt','小区RE参考功率':'RePower(0.1dbm)','运行状态的详细信息(DU小区配置)':'OnAirStatus','业务IP地址':'ServiceIP','站点类型':'Indoor'},inplace=True)

    Final_sheet_data['Indoor'].replace({'宏站':False,'室分':False,'微站':False},inplace=True)

    Final_sheet_data['HalfPowerAngle']=65

    usecols=['Longitude','Latitude','SiteName','CellName','ARFCN','PCI','Azimuth','gNBID','SectorID','CellID','TAC','MechanicalTilt','Height','ElectricalTilt','Indoor','HalfPowerAngle']

    real_data=Final_sheet_data[usecols]
    date_today=datetime.datetime.now().strftime("%Y%m%d%H%m")
    with open(os.path.join(current_path,'Spark5G工参_'+date_today+'.txt'),'w',encoding='UTF-8') as outputfile:
        real_data.to_string(outputfile,header=True, index=False, na_rep='NaN')
    outputfile.close()

    real_data.to_csv(os.path.join(current_path,'Spark5G工参_'+date_today+'.csv'),header=True, index=False,sep=',')
    return usecols

#to_string(buf=None, columns=None, col_space=None, header=True, index=True, na_rep='NaN', formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, max_rows=None, min_rows=None, max_cols=None, show_dimensions=False, decimal='.', line_width=None)

if __name__=="__main__":
    cols=spark_ProjectParameter=ProjectParameter_create_for_Spark()
    print('Spark工参已制作完毕,保存在当前路径下,请注意查看.')
    print('字段信息如下:\n',cols)
    input("Press EnterKey to Close the Window!")



