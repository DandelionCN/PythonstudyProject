#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 10:58:04 2019

@author: dandelion

"工具当前目录第一个excel文件必须为原始工参表,或者当前路径仅有工参表一个EXCEL文件"

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

    usecol_MirocSite = (
        "精品区分类",
        "站点类型",
        "簇归属",
        "gNBID",
        "CellID",
        "CGI",
        "SectorID",
        "PCI",
        "NEW PLAN PCI",
        "SiteName",
        "CellName",
        "中心频率",
        "中心频点",
        "SSB_Frequency",
        "SSB_ARFCN",
        "BandIndication",
        "BandWidth",
        "TAC",
        "Height",
        "Azimuth",
        "机械方位角",
        "波束方位角",
        "水平波束宽度",
        "垂直波束宽度",
        "DownTilt",
        "机械下倾角",
        "波束下倾角",
        "NRBBU经度",
        "NRBBU纬度",
        "NRAAU经度",
        "NRAAU纬度",
        "是否拉远",
        "小区运行状态",
        "小区RE参考功率",
        "工程进展",
        "管理IP",
        "业务IP",
        "锚点小区ECI_PCI列表",
        "好点上传速率",
        "好点下载速率",
        "单验测试结果",
        "测试日期"
    )

    sheet_data_MicroSite = pd.read_excel(
        project_parameter_table_fullname,
        sheet_name=sheetname_list[1],
        header=0,
        index_col=None,
        usecols=usecol_MirocSite,
        engine=None,
        #        skiprows=1
    )

    #    CGI_split = sheet_data["CGI"].str.split(pat="-", expand=True)
    #    CGI_split.columns = ["MCC", "MNC", "gNBID", "CellID"]
    #    Final_sheet_data = sheet_data.join(CGI_split)
    #    Final_sheet_data["SectorID"] = Final_sheet_data["CellID"]

    Data_Concate_Macro_Micro = pd.concat(
        [sheet_data_MacroSite, sheet_data_MicroSite], axis=0, ignore_index=True
    )
    #    获取当前时间用于文件命名
    date_today = datetime.datetime.now().strftime("%Y%m%d%H%m")

    #    宏站和室分合并数据表导出(室分保留PRU级别经纬度,不按CGI去重)
    Data_Concate_Macro_Micro.to_excel(
        os.path.join(current_path, "5G工参宏站室分合并PRU级_" + date_today + ".xlsx"),
        sheet_name="NR",
        header=True,
        index=False,
        engine="xlsxwriter",
        encoding="gbk"
    )

    #    按CGI对室分小区进行去重,剔除PRU级别数据,保留小区级数据
    Final_sheet_data = Data_Concate_Macro_Micro.drop_duplicates(
        subset=["CGI"], keep="first", inplace=False
    )

    #    宏站和室分合并数据表导出(室分保留PRU级别经纬度,不按CGI去重)
    Final_sheet_data.to_excel(
        os.path.join(current_path, "5G工参宏站室分合并小区级_" + date_today + ".xlsx"),
        sheet_name="NR",
        header=True,
        index=False,
        engine="xlsxwriter",
        encoding="gbk"
    )

    #    按照SPARK工参字段名称对表头字段进行重命名
    Final_sheet_data.rename(
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

    Final_sheet_data["Indoor"].replace(
        {"宏站": False, "室分": True, "微站": False}, inplace=True
    )

    #    sPARK工参字段
    usecols = [
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

    real_data = Final_sheet_data[usecols]

    #    导出SPARK工参表为EXCEL格式保存在当前路径下
    real_data.to_excel(
        os.path.join(current_path, "Spark5G工参_" + date_today + ".xlsx"),
        sheet_name="NR",
        header=True,
        index=False,
        engine="xlsxwriter",
        encoding="gbk"
    )

    return usecols


if __name__ == "__main__":
    cols = spark_ProjectParameter = ProjectParameter_create_for_Spark()
    print("Spark工参已制作完毕,保存在当前路径下,请注意查看.")
    print("字段信息如下:\n", cols)
    input("Press EnterKey to Close the Window!")
