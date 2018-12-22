# -*- coding: utf-8 -*-
"""
Title:
	Func_Get_CurDir_and_Subdir_filelist_with_oswalk
	
Created on Thu Aug  2 16:21:44 2018

@author: admin
------------------------------------------------
函数说明：
get_currentdir_and_subdir_filename(path, filetype, file_withpath_flag):
    #函数功能：本函数用于获取当前路径及子目录下所有文件的文件名称，以list格式输出；
    # path:指示当前文件夹路径
    # filetype：指示过滤的文件类型
    # file_withdir_flag：指示输出的文件列表是否携带文件的完整路径，1代表携带，其他代表不携带路径，仅输出文件名字。
    #file_withpath_flag=1时，函数输出结果为携带绝对路径的完成文件名称清单full_name；
    #file_withpath_flag<>1时，函数输出结果为不携带绝对路径的简单文件名称清单,base_name；
----------------------------
使用的主要方法说明：    
for root, dirs, files in os.walk(path):
    root:当前目录路径 ，会循环遍历当前路径及当前路径下的各个子文件夹，所以当前路径下的所有文件夹个数为root-1；
    files：当前路径下所有非目录子文件,返回当前path路径下的所有文件名称；
    dirs：当前路径下所有子目录(文件夹名称)清单    
"""
import os


def get_currentdir_and_subdir_filename(path, filetype, file_withpath_flag):
    # path:指示当前文件夹路径
    # filetype：指示文件类型
    # file_withdir_flag：指示输出的文件列表是否携带文件的完整路径，1代表携带，其他代表不携带路径，仅输出文件名字
    file_name_list = []
    file_name_listt_withdir = []
    dirs_name_list = []
    dir_sequence = 0
    # 以上3个公共变量，可遍历统计当前路径下的所有文件清单及目录清单
    for root, dirs, files in os.walk(path):
        print(str(dir_sequence), "当前路径root：\n{}".format(root))
        print("当前路径下的文件files：\n{}".format(files))
        print("当前路径下的文件夹dirs：\n{}".format(dirs))
        print("------------------------")
        dirs_name_list.append(root)
        dir_sequence += 1
        for i in files:  # 过滤文件类型
            if filetype in i:
                file_name_list.append(i)  # 逐个存入列表中
                file_name_listt_withdir.append(os.path.join(root, i))
        print("++++++++++++++++++++++++")
    print("当前路径的csv格式文件清单name：\n", file_name_list)
    print("当前路径的csv格式文件清单name_withdir:\n", file_name_listt_withdir)
    print("当前路径的文件夹个数为：", dir_sequence - 1)
    print(
        "当前路径的共有{}个文件夹，文件夹清单为:\n{}".format(len(dirs_name_list) - 1, dirs_name_list[1:])
    )
    if file_withpath_flag == 1:
        return file_name_listt_withdir
    else:
        return file_name_list


if __name__ == "__main__":
    print('==========================================================================')
    print('Better Tool,Better Future! Welcome to use CPE_LMT_CSVLog_Process tool!')
    print('--------------------------------------------------------------------------')
    print('Author:Dandelion|Contact:490359939@qq.com|All rights reserved!' )
    print('--------------------------------------------------------------------------')
    print('Attention Please:Make sure your file directory has no Chinese Characters!')
    data_path = r"C:\Users\admin\Desktop\tt"  # 指定数据源存放路径
    filter_filetype = ".csv"  # 指定数据源过滤格式
    print("================================================")
    file_list = get_currentdir_and_subdir_filename(data_path, filter_filetype, 0)
    print("当前路径下及子目录中格式为{}的文件如下：".format(filter_filetype))
    for files_item in file_list:
        print(files_item)
    print("================================================")
