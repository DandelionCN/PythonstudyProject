#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 23:21:35 2020

@author: dandelion
"""
import pandas as pd
import time
import os

# 定义函数
def export_dfs_to_excel_multisheet(excel_path, dict_sheetname_df):
    # input:
    # excel_path:保存的目标excel文件的全路径名称Full_name
    # dict_sheetname_df:字典型参数,内容为保存的sheetname:dataframe数据集,如:
    # {"sheetname1":df1,"sheetname2":df2,"sheetname3":df3,"sheetname4":df4}
    # output:
    # 保存不同的df数据至目标excel中的不同sheet中

    writer = pd.ExcelWriter(excel_path)
    for key in dict_sheetname_df:
        dict_sheetname_df[key].to_excel(writer, sheet_name=key, index=0)
    writer.save()
    writer.close()


if __name__ == "__main__":
    cur_date = time.strftime("%Y%m%d")
    cur_time = time.strftime("%Y%m%d_%H%M%S")
    save_path = os.path.join(os.getcwd(), cur_date + "导出数据_Result")
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    save_file = os.path.join(save_path, cur_time + "_multi_sheet.xlsx")

    source_data = os.path.join(os.getcwd(), "5G工参1119更新.xlsx")

    df1 = pd.read_excel(
        source_data,
        sheet_name="全网",
        header=0,
        index_col=None,
        usecols=None,
        engine=None,
    ).head(10)

    df2 = df1.copy().head(3)
    dic_df_sheetname = {"5g": df1, "4g": df2}
    export_dfs_to_excel_multisheet(save_file, dic_df_sheetname)


# writer=pd.ExcelWriter('filename.xlsx')
# ...
# df1.to_excel(writer,sheet_name='第一表',index=0)
# df2.to_excel(writer,sheet_name='第二表',index=0) #index=0：无索引
# writer.save()
# writer.close()


"""
向现有excel追加一条数据

df= pd.DataFrame(pd.read_excel('test.xlsx')) #读取原数据
df_rows = df.shape[0] #获取行数
#增加一条数据
df.loc[df_rows] = [a1 , b2 , c3 , d4] #与原数据同格式
df.to_excel('test.xlsx', sheet_name='sheet1', index=False, header=True)
-------------------------------------------------
批量修改datafram中某一列
如要对df中列名为“values”的值做修改，大于等于50改为1，小于50改为0，可用apply函数来实现：

复制代码
def fun(x):
    if x >= 50:
        return 1
    else:
        return 0

df['values'] = df['values'].apply(lambda x: fun(x))


"""
