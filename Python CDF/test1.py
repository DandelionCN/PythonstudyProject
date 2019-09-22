#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 15:30:55 2018

@author: admin
"""

import pandas as pd
#import numpy as np
import os

def do_operation():
    data_path = r"C:\Users\admin\Desktop\tt"
    filter_filetype = ".csv"
    # 在原始数据路径下新建结果数据保存路径...\..\Result
    uelog_result_savedir = make_uelog_result_savedir(data_path)
    # 使用原始数据文件列表获取函数，获取文件名称列表，文件名称包含完整路径
    filter_filelist = get_filename(data_path, filter_filetype, 1)
    print(filter_filelist)
    # 基于原始log，逐个进行数据处理，处理完毕将结果数据以CSV格式保存在Result文件夹中
    # 结果数据命名规则为：原始文件名_result.csv
    for filex in filter_filelist:
        uelog=pd.read_csv(filex,sep=',',header=0)
        filex_result_name = os.path.basename(filex).strip()[:-4]
        filex_result_full_name = os.path.join(uelog_result_savedir, filex_result_name)+"_result.csv"
#        filex_result_full_name = os.path.join(uelog_result_savedir, filex_result_name)+ '_'+str(np.random.randint(10,100))+"_result.csv"
        uelog.to_csv(filex_result_full_name,sep=',',header=True,index=False)
        
    
    print("一共有{}个Log，已处理完毕，结果如下，请到如上路径查看!".format(len(filter_filelist)))
    for results in get_filename(uelog_result_savedir, filter_filetype, 0):
        print(results)   
        
def make_uelog_result_savedir(sourcedata_path):
    uelog_result_savedir = os.path.join(sourcedata_path, "Result")
    pathisExists = os.path.exists(uelog_result_savedir)
    if not pathisExists:
        os.mkdir(os.path.join(sourcedata_path, "Result"))
        print("已新建结果数据保存路径为：\n{}".format(uelog_result_savedir))
    else:
        print("结果数据保存路径已经存在，路径为：\n{}".format(uelog_result_savedir))
    return uelog_result_savedir


# 定义函数get_filename（），用于获取制定路径下制定格式的文件名清单，存入列表中
def get_filename(path, filetype, file_withpath_flag):
    # path:指示当前文件夹路径
    # filetype：指示文件类型
    # file_withdir_flag：指示输出的文件列表是否携带文件的完整路径，1代表携带，其他代表不携带路径，仅输出文件名字
    name = []
    name_withdir = []
    for root, dirs, files in os.walk(path):
        print('当前路径root：\n{}'.format(root))
        print('当前路径files：\n{}'.format(files))
        print('当前路径下的dirs：\n{}'.format(dirs))
        for i in files:  # 过滤文件类型
            if filetype in i:
                name.append(i)  # 逐个存入列表中
                name_withdir.append(os.path.join(path, i))
    if file_withpath_flag == 1:
        return name_withdir
    else:
        return name


if __name__ == "__main__":
    do_operation()

