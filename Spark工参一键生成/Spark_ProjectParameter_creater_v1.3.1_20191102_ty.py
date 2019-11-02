#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 10:58:04 2019

@author: dandelion

"工具当前目录第一个excel文件必须为原始工参表,或者当前路径仅有工参表一个EXCEL文件"
"第一个sheet内容为NR工参表,第二sheet内容为FDD工参表";

NR-spark字段:['Longitude', 'Latitude', 'SiteName', 'CellName', 'ARFCN', 'PCI', 'Azimuth', 'gNBID', 'SectorID', 'CellID', 'TAC', 'MechanicalTilt', 'Height', 'ElectricalTilt', 'Indoor', 'HalfPowerAngle']

LTE-spark字段:['Longitude', 'Latitude', 'SiteName', 'CellName', 'EARFCN', 'PCI', 'Azimuth', 'eNodeBID', 'SectorID', 'CellID', 'TAC', 'MechanicalTilt', 'Height', 'ElectricalTilt', 'Indoor', 'HalfPowerAngle']

"""

import os
import xlrd
import pandas as pd
import datetime
import xlsxwriter


def ProjectParameter_create_for_Spark():
    current_path = os.getcwd()
    files_list = os.listdir(current_path)
    # print(files_list)
    file_name = []
    for files in files_list:
        if ".xls" in files:
            file_name.append(files)
            break

    project_parameter_table_fullname = os.path.join(current_path, file_name[0])
    print("工参表路径及名称为:\n", project_parameter_table_fullname)

    # 获取sheetnames
    workbook = xlrd.open_workbook(project_parameter_table_fullname)
    sheetname_list = workbook.sheet_names()
    print("Sheetname清单为:\n", sheetname_list)

    # sheet_data=workbook.sheet_by_name[sheetname_list[0]]

    sheet_data_MacroSite = pd.read_excel(
        project_parameter_table_fullname,
        sheet_name=sheetname_list[0],
        header=0,
        index_col=None,
        usecols=None,
        engine=None,
    )


#    sheet_data_MicroSite = pd.read_excel(
#        project_parameter_table_fullname,
#        sheet_name=sheetname_list[1],
#        header=0,
#        index_col=None,
#        usecols=None,
#        engine=None,
#        #        skiprows=1
#    )

    sheet_data_FDD = pd.read_excel(
        project_parameter_table_fullname,
        sheet_name=sheetname_list[1],
        header=0,
        index_col=None,
        usecols=None,
        engine=None,
        #        skiprows=1
    )

    Final_sheet_data_NR=sheet_data_MacroSite
    Final_sheet_data_FDD=sheet_data_FDD
    #    CGI_split = sheet_data["CGI"].str.split(pat="-", expand=True)
    #    CGI_split.columns = ["MCC", "MNC", "gNBID", "CellID"]
    #    Final_sheet_data = sheet_data.join(CGI_split)
    #    Final_sheet_data["SectorID"] = Final_sheet_data["CellID"]


    #    按照SPARK工参字段名称对NR表头字段进行重命名
    Final_sheet_data_NR.rename(
        columns={
            "站点类型": "Indoor",
            "SSB_ARFCN":"ARFCN",
            "水平波束宽度":"HalfPowerAngle",
            "机械下倾角":"MechanicalTilt",
            "波束下倾角":"ElectricalTilt",
            "NRAAU经度":"Longitude",
            "NRAAU纬度":"Latitude",
            "小区运行状态":"OnAirStatus"
        },
        inplace=True,
    )

    Final_sheet_data_NR["Indoor"].replace(
        {"宏站": 0, "室分": 1, "微站": 0}, inplace=True
    )

    #    sPARK工参字段
    usecols_NR = [
        "Longitude",
        "Latitude",
        "SiteName",
        "CellName",
        "ARFCN",
        "PCI",
        "Azimuth",
        "gNBID",
        "SectorID",
        "CellID",
        "TAC",
        "MechanicalTilt",
        "Height",
        "ElectricalTilt",
        "Indoor",
        "HalfPowerAngle",
        "OnAirStatus",
        "CGI"
    ]

    #按照SPARK工参字段名称对FDD表头字段进行重命名
    Final_sheet_data_FDD.rename(
        columns={
            "站号":"eNodeBID",
            "基站名称":"SiteName",
            "小区名称":"CellName",
            "E-UTRAN TDD小区ID":"SectorID",
            "小区标识":"CellID",
            "机械下倾角":"MechanicalTilt",
            "电子下倾角":"ElectricalTilt",
            "天线挂高(米)":"Height",
            "物理小区识别码":"PCI",
            "频点":"EARFCN",
            "跟踪区码":"TAC"
        },
        inplace=True,
    )
    Final_sheet_data_FDD["Indoor"]=0
    Final_sheet_data_FDD["HalfPowerAngle"]=65


    usecols_FDD = [
        "Longitude",
        "Latitude",
        "SiteName",
        "CellName",
        "EARFCN",
        "PCI",
        "Azimuth",
        "eNodeBID",
        "SectorID",
        "CellID",
        "TAC",
        "MechanicalTilt",
        "Height",
        "ElectricalTilt",
        "Indoor",
        "HalfPowerAngle",
        "ECI"
    ]


    real_data_NR = Final_sheet_data_NR[usecols_NR]
    real_data_FDD = Final_sheet_data_FDD[usecols_FDD]
    date_today = datetime.datetime.now().strftime("%Y%m%d%H%m")

    #    导出SPARK工参表为EXCEL格式保存在当前路径下
    real_data_NR.to_excel(
        os.path.join(current_path, "Spark5G工参_" + date_today + ".xlsx"),
        sheet_name="NR",
        header=True,
        index=False,
        engine="xlsxwriter",
        encoding="gbk"
    )

    real_data_FDD.to_excel(
        os.path.join(current_path, "Spark4G工参_" + date_today + ".xlsx"),
        sheet_name="FDD",
        header=True,
        index=False,
        engine="xlsxwriter",
        encoding="gbk"
    )

    return usecols_NR,usecols_FDD


if __name__ == "__main__":
    cols_NR,cols_FDD = spark_ProjectParameter = ProjectParameter_create_for_Spark()
    print("Spark工参已制作完毕,保存在当前路径下,请注意查看.")
    print("NR_spark字段信息如下:\n", cols_NR)
    print("FDD_spark字段信息如下:\n", cols_FDD)
    input("Press EnterKey to Close the Window!")





