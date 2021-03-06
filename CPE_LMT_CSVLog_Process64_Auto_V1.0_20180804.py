#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Title:
	CPE_LMT_CSVLog_Process64_Auto_V1.0_20180804

Created on Fri Aug  3 21:05:43 2018

@author: admin

执行顺序：
1:执行get_souce_log()函数，获取输入数据，调用数据处理函数和保存数据函数
2:调用uelog_operate()过程，处理log
3:调用make_uelog_result_savedir()函数，创建数据保存目录
特色功能：
启动程序后，将log文件批量拖入程序窗口，回车后，程序自动进行数据处理和保存，交互式退出程序。

Attention:
    please use english file directory ,otherwise there will be some errors.


"""
import pandas as pd
import os


def get_souce_log():
    file_path_list = (
        (input("Please Pull all the source files to the window:\n"))
        .strip()
        .replace("'", "")
        .split(",")
    )
    if file_path_list[0] == "":
        print("没有Log输入!")
    else:
        for file_x in file_path_list:
            file_path = file_x.strip()
            uelog_operate(file_path)
        print(
            "结果数据保存路径为：\n{}".format(
                make_uelog_result_savedir(os.path.dirname(file_path_list[0]))
            )
        )


def uelog_operate(uelog_fullname):
    df_data = pd.read_csv(uelog_fullname, sep=",", header=0)
    # cols=df_data.columns.values
    # print(cols)
    # 字段计算公式制定
    df_data["CSIrsrp_Average"] = df_data.apply(
        lambda x: (x["CSIRsrp_1"] + x["CSIRsrp_2"] + x["CSIRsrp_3"] + x["CSIRsrp_4"])
        / 4,
        axis=1,
    )

    df_data["CSISinr_Average"] = df_data.apply(
        lambda x: (x["CSISinr_1"] + x["CSISinr_2"] + x["CSISinr_3"] + x["CSISinr_4"])
        / 4,
        axis=1,
    )

    df_data["SSBlockSinr_Average"] = df_data.apply(
        lambda x: (
            x["SSBlockSinr_1"]
            + x["SSBlockSinr_2"]
            + x["SSBlockSinr_3"]
            + x["SSBlockSinr_4"]
        )
        / 4,
        axis=1,
    )

    df_data["ULThroughput_Total"] = df_data.apply(
        lambda x: (x["ULThroughput_1"] + x["ULThroughput_2"]) / 1024, axis=1
    )

    df_data["DLThroughput_Total"] = df_data.apply(
        lambda x: (
            x["DLThroughput_1"]
            + x["DLThroughput_2"]
            + x["DLThroughput_3"]
            + x["DLThroughput_4"]
        )
        / 1024,
        axis=1,
    )

    df_data["NCell1SSBRsrp_Average"] = df_data.apply(
        lambda x: (
            x["NCell1SSBRsrp_1"]
            + x["NCell1SSBRsrp_2"]
            + x["NCell1SSBRsrp_3"]
            + x["NCell1SSBRsrp_4"]
            + x["NCell1SSBRsrp_5"]
            + x["NCell1SSBRsrp_6"]
            + x["NCell1SSBRsrp_7"]
            + x["NCell1SSBRsrp_8"]
        )
        / 8,
        axis=1,
    )

    df_data["NCell2SSBRsrp_Average"] = df_data.apply(
        lambda x: (
            x["NCell2SSBRsrp_1"]
            + x["NCell2SSBRsrp_2"]
            + x["NCell2SSBRsrp_3"]
            + x["NCell2SSBRsrp_4"]
            + x["NCell2SSBRsrp_5"]
            + x["NCell2SSBRsrp_6"]
            + x["NCell2SSBRsrp_7"]
            + x["NCell2SSBRsrp_8"]
        )
        / 8,
        axis=1,
    )

    df_data["ULMcs_Average"] = df_data.apply(
        lambda x: (x["ULMcs_1"] + x["ULMcs_2"]) / 2, axis=1
    )

    df_data["PuschBler_Average"] = df_data.apply(
        lambda x: (x["PuschBler_1"] + x["PuschBler_2"]) / 2, axis=1
    )

    df_data["DLMcs_Average"] = df_data.apply(
        lambda x: (x["DLMcs_1"] + x["DLMcs_2"] + x["DLMcs_3"] + x["DLMcs_4"]) / 2,
        axis=1,
    )

    df_data["PdschBler_Average"] = df_data.apply(
        lambda x: (
            x["PdschBler_1"] + x["PdschBler_2"] + x["PdschBler_3"] + x["PdschBler_4"]
        )
        / 4,
        axis=1,
    )

    # 需求字段提取及输出
    # output_data=df_data[['Time','GPSTime','GPSLong','GPSLA','GPSHeigh','Ue Id','Pci','ULRbNum','TxPwr','CRNTI','DLRbNum','MIMOMod','CQI','PbchCrcErrorNum','PbchCrcSuccNum','PbchCrcSucc_Scale','OptimalAvgRSRP','CSIrsrp_Average','CSISinr_Average','SSBlockSinr_Average','ULMcs_Average','PuschBler_Average','ULThroughput_Total','DLMcs_Average','PdschBler_Average','DLThroughput_Total','NCell1Pci','NCell1SSBRsrp_Average'
    # ,'NCell2Pci','NCell2SSBRsrp_Average']]

    # output_data=df_data[['Time','GPSTime','GPSLong','GPSLA','CSIrsrp_Average','CSISinr_Average','SSBlockSinr_Average','ULThroughput_Total','DLThroughput_Total','Ue Id','Pci','ULRbNum','TxPwr','CRNTI','DLRbNum','MIMOMod','CQI','PbchCrcErrorNum','PbchCrcSuccNum','PbchCrcSucc_Scale','OptimalAvgRSRP','ULMcs_Average','PuschBler_Average','DLMcs_Average','PdschBler_Average','NCell1Pci','NCell1SSBRsrp_Average','NCell2Pci','NCell2SSBRsrp_Average','GPSHeigh']]

    output_data = df_data[
        [
            "Time",
            "Ue Id",
            "GPSLong",
            "GPSLA",
            "CSIrsrp_Average",
            "CSISinr_Average",
            "SSBlockSinr_Average",
            "ULThroughput_Total",
            "DLThroughput_Total",
            "Pci",
            "ULRbNum",
            "CRNTI",
            "DLRbNum",
            "MIMOMod",
            "CQI",
            "PbchCrcErrorNum",
            "PbchCrcSuccNum",
            "PbchCrcSucc_Scale",
            "OptimalAvgRSRP",
            "ULMcs_Average",
            "PuschBler_Average",
            "DLMcs_Average",
            "PdschBler_Average",
            "NCell1Pci",
            "NCell1SSBRsrp_Average",
            "NCell2Pci",
            "NCell2SSBRsrp_Average",
            "GPSHeigh",
        ]
    ]

    #    savefile_fullname=os.path.dirname(uelog_fullname)+'/Result/'+(os.path.basename(uelog_fullname)[:-4])+'_Result.csv'
    uelog_dir = os.path.dirname(uelog_fullname)
    uelog_save_dir = make_uelog_result_savedir(uelog_dir)
    #    print("结果数据保存路径为：\n{}".format(make_uelog_result_savedir(uelog_dir)))
    savefile_fullname = os.path.join(
        uelog_save_dir, (os.path.basename(uelog_fullname)[:-4]) + "_Result.csv"
    )
    output_data.to_csv(savefile_fullname, sep=",", header=True, index=False)


def make_uelog_result_savedir(sourcedata_path):
    uelog_result_savedir = sourcedata_path + "/Result"
    pathisExists = os.path.exists(uelog_result_savedir)
    if not pathisExists:
        os.mkdir(os.path.join(sourcedata_path, "Result"))
    #        print("已新建结果数据保存路径为：\n{}".format(uelog_result_savedir))
    #    else:
    #        print("结果数据保存路径已经存在，路径为：\n{}".format(uelog_result_savedir))
    return uelog_result_savedir


if __name__ == "__main__":
    print('==========================================================================')
    print('Better Tool,Better Future! Welcome to use CPE_LMT_CSVLog_Process tool!')
    print('--------------------------------------------------------------------------')
    print('Author:DandelionCN|Contact:****@qq.com|All rights reserved!' )
    print('--------------------------------------------------------------------------')
    print('Attention Please:Make sure your file directory has no Chinese Characters!')
    print('==========================================================================')
    get_souce_log()
    stop_flag = str(
        input("Operation completed,Do you want to eixt?( y/n):").strip()
    ).upper()
    while stop_flag == "N":
        get_souce_log()
        stop_flag = str(
            input("Operation completed,Do you want to eixt? y/n:").strip()
        ).upper()
    input("Press EnterKey to Close the Window!")
