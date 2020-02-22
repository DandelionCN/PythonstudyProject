#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
the input file_directory named as [Source_Log_Exported_From_Spark] in the current path with the source python file
~/Source_Log_Exported_From_Spark
"""

import pandas as pd
import os

# import datetime
import time

# import seaborn as sns
# import matplotlib.pyplot as plt


def Export_data_to_excel(Save_DataFrame, Save_Workbookname, Save_Sheetname):
    date_today = time.strftime("%Y%m%d_%H%M%S")
    Save_DataFrame.to_excel(
        os.path.join(Save_dir, Save_Workbookname + "_" + date_today + ".xlsx"),
        sheet_name=Save_Sheetname,
        header=True,
        index=True,
        engine="xlsxwriter",
        encoding="gbk",
    )
    print(Save_Workbookname + "is Created successfully!")


def read_and_comb_data_from_spark_csv(spark_csv_dir):
    files_list = os.listdir(spark_csv_dir)
    csv_file_list = []
    file_num = 0
    for files in files_list:
        if ".csv" in files:
            df_read_from_csv = pd.read_csv(
                os.path.join(spark_csv_dir, files), header=0, encoding="gbk"
            )
            csv_file_list.append(df_read_from_csv)
            file_num += 1
    print("共读入{}个原始log!".format(file_num))
    csv_comb = pd.concat(csv_file_list)
    csv_comb.drop_duplicates(inplace=True)
    csv_comb.dropna(how="all", inplace=True)
    csv_comb.dropna(subset=["NR MAC Thr. DL [Mbps]"], inplace=True)
    csv_comb.dropna(axis=1, how="all", inplace=True)
    csv_comb = csv_comb[(~csv_comb["NR DMRS RSRP[dBm]"].isin(["-∞"]))]
    csv_comb[["NR DMRS RSRP[dBm]"]] = csv_comb[["NR DMRS RSRP[dBm]"]].astype(float)
    return csv_comb


def data_process(csv_data_df):
    csv_data_df.rename(columns={"Time": "caiyangdian"}, inplace=True)
    dict_map = {
        "NR PCI": "mean",
        "caiyangdian": "count",
        "NR MAC Thr. DL [Mbps]": "mean",
        "SS RSRP[dBm]": "mean",
        "NR DMRS RSRP[dBm]": "mean",
        "SS SINR[dB]": "mean",
        "NR DMRS SINR[dB]": "mean",
        "NR MCS Avg. DL": "mean",
        "NR PDSCH RBCountPerSlot": "mean",
        "NR PDCCH DL Grant Count": "mean",
        "NR PDSCH iBLER[%]": "mean",
        "NR PUSCH iBLER[%]": "mean",
        "NR Rank AVG DL": "mean",
        "NR MCS Avg. UL": "mean",
        "NR PathLoss": "mean",
        "PDCP Thr. DL [Mbps]": "mean",
        "PDCP Thr. UL [Mbps]": "mean",
    }
    data_agg = csv_data_df.groupby("NR小区名").agg(dict_map)
    data_agg.sort_values(by="NR MAC Thr. DL [Mbps]", ascending=True, inplace=True)
    return data_agg


def Low_Speed_Bad_Cell(DT_Log_Df):
    caiyangdian_thres_base = 100
    caiyangdian_thres_low = 20
    Low_speed_thres = 200
    Low_speed_thres_UL = 15
    UL_high_BLER_thres = 15
    DL_high_BLER_thres = 15
    Low_sinr_thres = 0
    High_sinr_thres = 5
    Low_DL_mcs_thres = 5
    Delt_SSB_CSI = 10
    pd.set_option("mode.chained_assignment", None)

    #    1.高采样点占比低速率小区
    low_speed_and_more_use_cell = DT_Log_Df[
        (
            (DT_Log_Df["caiyangdian"] > caiyangdian_thres_base)
            & (DT_Log_Df["NR MAC Thr. DL [Mbps]"] > Low_speed_thres)
            & (DT_Log_Df["PDCP Thr. UL [Mbps]"] > Low_speed_thres_UL)
        )
    ]
    if low_speed_and_more_use_cell.shape[0] > 0:
        low_speed_and_more_use_cell.loc[:, "问题分类"] = "高采样点占比低速率小区"

    #    2.上下行高BLER小区
    DLUL_high_bler_cell = DT_Log_Df[
        (
            (DT_Log_Df["caiyangdian"] > caiyangdian_thres_base)
            & (
                (DT_Log_Df["NR PDSCH iBLER[%]"] > DL_high_BLER_thres)
                | (DT_Log_Df["NR PUSCH iBLER[%]"] > UL_high_BLER_thres)
            )
        )
    ]
    if DLUL_high_bler_cell.shape[0] > 0:
        DLUL_high_bler_cell.loc[:, "问题分类"] = "上下行高BLER小区"

    #    3.低SINR小区
    low_ssbsinr_cell = DT_Log_Df[
        (
            (DT_Log_Df["caiyangdian"] > caiyangdian_thres_base)
            & (DT_Log_Df["SS SINR[dB]"] < Low_sinr_thres)
        )
    ]
    if low_ssbsinr_cell.shape[0] > 0:
        low_ssbsinr_cell.loc[:, "问题分类"] = "低SSB_SINR小区"

    #    4.高BLER&低MCS小区(D频段干扰)
    high_sinr_low_mcs_cell = DT_Log_Df[
        (
            (DT_Log_Df["caiyangdian"] > caiyangdian_thres_base)
            & (DT_Log_Df["SS SINR[dB]"] > High_sinr_thres)
            & (DT_Log_Df["NR MCS Avg. DL"] < Low_DL_mcs_thres)
        )
    ]
    if high_sinr_low_mcs_cell.shape[0] > 0:
        high_sinr_low_mcs_cell.loc[:, "问题分类"] = "高SSB_SINR低MCS小区"

    #    5.低采样点占比小区
    less_use_cell = DT_Log_Df[(DT_Log_Df["caiyangdian"] > caiyangdian_thres_low)]
    if less_use_cell.shape[0] > 0:
        less_use_cell.loc[:, "问题分类"] = "低采样点占比小区"

    #    6.CSI(DMRS)与SSB覆盖差异过大小区
    DMRS_SSB_coverage_diff_cell = DT_Log_Df[
        (abs(DT_Log_Df["SS RSRP[dBm]"] - DT_Log_Df["NR DMRS RSRP[dBm]"]) > Delt_SSB_CSI)
    ]
    if DMRS_SSB_coverage_diff_cell.shape[0] > 0:
        DMRS_SSB_coverage_diff_cell.loc[:, "问题分类"] = "DMRS与SSB覆盖差异过大小区"
    # 合并各类问题小区
    bad_cell_com = low_speed_and_more_use_cell.append(
        [
            DLUL_high_bler_cell,
            low_ssbsinr_cell,
            high_sinr_low_mcs_cell,
            less_use_cell,
            DMRS_SSB_coverage_diff_cell,
        ]
    )
    return bad_cell_com


def export_df_to_multi_excel_sheet(save_excel_file, dict_sheet_name_df):
    #    讲多个dateframe数据导出到同一个Excel工作薄的不同sheet中
    writer = pd.ExcelWriter(save_excel_file)
    for key in dict_sheet_name_df:
        print("正在导出数据", key)
        dict_sheet_name_df[key].to_excel(
            writer, sheet_name=key, index=True, header=True, encoding="gbk"
        )
    print("正在保存数据中......")
    writer.save()
    writer.close()
    print("所有数据已导出成功,请注意查看.")


if __name__ == "__main__":
    print("Welcome to use LowSpeedAnalysis Tool!")
    print("The process is strating now.......")
    try:
        date_today = time.strftime("%Y%m%d")
        time_now = time.strftime("%Y%m%d%H%M%S")
        Save_dir = os.path.join(
            os.getcwd(), date_today + "_Bad_Cell_list_From_Spark_log"
        )
        if not os.path.exists(Save_dir):
            os.mkdir(Save_dir)
            print("The save directory is created successfully in the current path!")
        else:
            print("The save directory is already exist!")
    except:
        print("Run Error!")
    Save_Excel_File = os.path.join(Save_dir, time_now + "_BadCellList.xlsx")
    spark_csv_dir = os.path.join(os.getcwd(), "Source_Log_Exported_From_Spark")
    all_data = read_and_comb_data_from_spark_csv(spark_csv_dir)
    all_data_title = all_data.columns.to_list()
    print("The columns name are:\n", all_data_title)
    print(all_data.describe())
    dt_cell_in_use = data_process(all_data)
    col_list = [
        "NR MAC Thr. DL [Mbps]",
        #        "SS RSRP[dBm]",
        "SS SINR[dB]",
        #        "NR DMRS SINR[dB]",
        "NR MCS Avg. DL",
        "NR PDSCH RBCountPerSlot",
        #        "NR PDCCH DL Grant Count",
        "NR PDSCH iBLER[%]",
        #        "NR PUSCH iBLER[%]",
        #        "NR Rank AVG DL",
        "NR PathLoss",
    ]
    bad_cell = Low_Speed_Bad_Cell(dt_cell_in_use)
    dict_sheetname_dfs = {
        "差小区清单": bad_cell,
        "测试指标概况": all_data.describe(),
        "测试路线占用小区KPI指标": dt_cell_in_use,
        "采样点级合并log": all_data,
    }
    export_df_to_multi_excel_sheet(Save_Excel_File, dict_sheetname_dfs)
    #    sns.pairplot(dt_cell_in_use[col_list])
    #    plt.savefig(os.path.join(Save_dir, "下载速率相关性图.png"))
    print("保存路径为:\n", Save_dir)
    input("Press Enter key to Close the Window!")
