# -*- coding: utf-8 -*-
"""
Title:
	SelfTaxCalculation_64_V1.0_20180802
	
Created on Thu Aug  2 21:48:22 2018

@author: admin

​​实现一个个人所得税计算器。
输入月收入和五险一金计算个人所得税
Version: 0.1

Date: 2018

"""
def self_tax_calcution():
    salary = float(input("本月收入: ").strip())
    insurance = float(input("五险一金: ").strip())
    diff = salary - insurance - 3500
    if diff <= 0:
        rate = 0
        deduction = 0
    elif diff < 1500:
        rate = 0.03
        deduction = 0
    elif diff < 4500:
        rate = 0.1
        deduction = 105
    elif diff < 9000:
        rate = 0.2
        deduction = 555
    elif diff < 35000:
        rate = 0.25
        deduction = 1005
    elif diff < 55000:
        rate = 0.3
        deduction = 2755
    elif diff < 80000:
        rate = 0.35
        deduction = 5505
    else:
        rate = 0.45
        deduction = 13505
    tax = abs(diff * rate - deduction)
    print("个人所得税: ￥%.2f元" % tax)
    print("实际到手收入: ￥%.2f元" % (diff + 3500 - tax))
    
    
if __name__=="__main__":
    print('==========================================================================')
    print('Better Tool,Better Future! Welcome to use CPE_LMT_CSVLog_Process tool!')
    print('--------------------------------------------------------------------------')
    print('Author:Dandelion|Contact:490359939@qq.com|All rights reserved!' )
    print('--------------------------------------------------------------------------')
    print('Attention Please:Make sure your file directory has no Chinese Characters!')
    print('==========================================================================')
    self_tax_calcution()
    stop_flag=str(input("Do you want to eixt?( y/n):").strip()).upper()
    while stop_flag=='N':
        self_tax_calcution()
        stop_flag=str(input("Do you want to eixt? y/n:").strip()).upper()
    input("Press EnterKey to Close the Window!")
    

    
