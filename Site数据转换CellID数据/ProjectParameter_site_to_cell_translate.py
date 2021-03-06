#!/usr/bin/python3
# _*_ coding: utf_8 _*_
"""
Created on Mon Dec 22 22:24:00 2018

@author: dandelion
要求：第一列为gnbname，最后一列为以"/"连接的方位角组合列，如：20/150/300
"""

import xlrd
import xlwt

def readsheetbyname(filename,sheetname):
    """按照给定的sheetname列表读取excel中相应的sheet"""
    workbook=xlrd.open_workbook(filename,on_demand=True)
    booksheetnames=workbook.sheet_names()
    if sheetname in booksheetnames:
        sheet=workbook.sheet_by_name(sheetname)
        rows=[sheet.row_values(row) for row in range(sheet.nrows)]
        rowcount=sheet.nrows
        colcount=sheet.ncols
    return rows,rowcount,colcount


def site_to_cell_translate():
    sheet_content,rows_source_sheet,cols_source_sheet=readsheetbyname(excel_file_name,sheet_name)
    newlist=[]
    title=sheet_content[0]
    title.append("Cellname")
    newlist.append(title)
    print("table_title:",title)
    print("---------------------------------")
    for i in range(1,rows_source_sheet):
        split_list=str(sheet_content[i][-1]).split("/")
        for elemnts in split_list:
            sheet_content[i][-1]=elemnts
            cell_name=sheet_content[i][0]+"_NR_"+str(split_list.index(elemnts)+1)
            list_to_tuple=tuple(sheet_content[i])
            tuple_to_list=list(list_to_tuple)
            tuple_to_list.append(cell_name)
            newlist.append(tuple_to_list)
    print("Resultlist",newlist)
    #save the array to a new workbook
    save_workbook=xlwt.Workbook()
    save_sheet=save_workbook.add_sheet("Cell Project Parameter")
    rows_newlist=shape(newlist)[0]
    cols_newlist=shape(newlist)[1]
    for rows in range(rows_newlist):
        for cols in range(cols_newlist):
            save_sheet.write(rows,cols,newlist[rows][cols])
    save_workbook.save("/home/dandelion/文档/Cell Project Parameter.xlsx")

if __name__=="__main__":
    excel_file_name=input("please drag the file into this window:\n").replace("'","")
#    print(excel_file_name)
    #excel_file_name="/home/dandelion/zhandian.xlsx"
    sheet_name="gnb"    #sheet name of the source data
    site_to_cell_translate()




# =============================================================================
# #打开Excel工作薄的指定sheet，获取sheet对象及行数和列数
# def read_sheet_by_name(workbookname_with_full_path,sheet_name_to_open):
#     workbook_to_open=xlrd.open_workbook(workbookname_with_full_path)
#     sheet_to_open=workbook_to_open.sheet_by_name(sheet_name_to_open)
#     rowcount=sheet_to_open.nrows
#     colcount=sheet_to_open.ncols
#     return sheet_to_open,rowcount,colcount
#
# #sheet_process,nrows,ncols=(read_sheet_by_name(excel_file_name,sheet_name))
# #print(sheet_process)
# #print(nrows)
# #print(ncols)
# #读取sheet的多行数据
# def get_mutirows_from_sheet(sheet,start_rowx=0,end_rowx=0):
#     rows_value=[sheet.row_values(rowx) for rowx in range(start_rowx,end_rowx)]
#     return rows_value
#
# #print(get_mutirows_from_sheet(sheet_process,0,nrows))
#
# #读取sheet的多列数据
# def get_muticols_from_sheet(sheet,start_colx=0,end_colx=0):
#     cols_value=[sheet.col_values(colx) for colx in range(start_colx,end_colx)]
#     return cols_value
#
# #print(get_muticols_from_sheet(sheet_process,0,ncols))
# =============================================================================



# =============================================================================
# source code without function
# sheet_content,rows,cols=readsheetbyname(excel_file_name,sheet_name)
# #print("sheet_content:",sheet_content)
# #print("---------------------------------")
# newlist=[]
# title=sheet_content[0]
# #print(title)
# #title.insert(title.index('gname')+1,"Cellname")
# #print("new_title:",new_title)
# title.append("Cellname")
# newlist.append(title)
# print("table_name:",newlist)
# print("---------------------------------")
# for i in range(1,rows):
# #    print("old_row:",sheet_content[i])
#     split_list=str(sheet_content[i][-1]).split("/")
# #    print("split_list:",split_list)
#     for elemnts in split_list:
# #        print("current elemnts:",elemnts)
#         sheet_content[i][-1]=elemnts
# #        row_updated=sheet_content[i]
#         cell_name=sheet_content[i][0]+"_NR_"+str(split_list.index(elemnts)+1)
# #        sheet_content[i].append(cell_name)
# #        print("current_row:",sheet_content[i])
#         list_to_tuple=tuple(sheet_content[i])
#         tuple_to_list=list(list_to_tuple)
#         tuple_to_list.append(cell_name)
# #        print("list_to_tuple:",tuple_list)
#         newlist.append(tuple_to_list)
# #        print("current_newlist:",newlist)
# #    print("------------line close-----------------")
# print("newlist",newlist)
#
# save_workbook=xlwt.Workbook()
# save_sheet=save_workbook.add_sheet("Cell Project Parameter")
#
# rows_newlist=shape(newlist)[0]
# cols_newlist=shape(newlist)[1]
# for rows in range(rows_newlist):
#     for cols in range(cols_newlist):
#         save_sheet.write(rows,cols,newlist[rows][cols])
#
# save_workbook.save("/home/dandelion/Cell Project Parameter.xlsx")
# =============================================================================
