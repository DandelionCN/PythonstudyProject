#!/usr/bin/env python3
# _*_ coding: utf_8 _*_
"""
Created on Mon Dec  3 22:24:00 2018

@author: dandelion

N_REF=N_REF_Offs*1000+(F_REF-F_REF_Offs)*1000/Dlta_F_Global
F_REF = F_REF_Offs + Dlta_F_Global*10**(-3)*(N_REF-N_REF_Offs)


Frequency range (MHz)	ΔFGlobal (kHz)	FREF_Offs (MHz)	NREF_Offs	Range of NREF
0 – 3000	5	0	0	0 – 599999
3000 – 24250	15	3000	600000	600000 – 2016666
24250 – 100000	60	24250.08	2016667	2016667 – 3279165
------------------

"""

#   Calculation of 5G NR ARFCN from 5G NR frequency.
def NR_ARFCN_Calculate(F_REF):
    if F_REF<=3000:
        Dlta_F_Global=5
        F_REF_Offs=0
        N_REF_Offs=0
        N_REF_Range='0~599999'
    elif F_REF<=24250:
        Dlta_F_Global=15
        F_REF_Offs=3000
        N_REF_Offs=600000
        N_REF_Range='600000~2016666'
    else:
        Dlta_F_Global=60
        F_REF_Offs=24250.08
        N_REF_Offs=2016667
        N_REF_Range='2016667~3279165'
    N_REF=N_REF_Offs+(F_REF-F_REF_Offs)/(Dlta_F_Global*10**(-3))
    return round(N_REF),N_REF_Range


def FREQUENCY_to_NR_ARFCN():
    while True:
        try:
            Frequency=input("Please input the Frequency between (0,100000]MHz:\n")
            Frequency=float(Frequency)
            if 0<Frequency<=100000:
                NR_ARFCN,NR_ARFCN_Range=NR_ARFCN_Calculate(Frequency)
                print("The NR_ARFCN of the Frequency is:",NR_ARFCN)
                print("It belongs to the range:",NR_ARFCN_Range)
                break
            else:
                print("The input value should be between (0,100000].Try again!")
        except:
            print("Invalid input,Value should be between (0,100000]MHz,Try again!")

#================================================================================
#   Calculation of 5G NR frequency from 5G NR ARFCN.
def NR_Frequcency_Calculate(N_REF):
    if N_REF<=599999:
        Dlta_F_Global=5
        F_REF_Offs=0
        N_REF_Offs=0
        F_REF_Range='0~3000'
    elif N_REF<=2016666:
        Dlta_F_Global=15
        F_REF_Offs=3000
        N_REF_Offs=600000
        F_REF_Range='3000~24250'
    else:
        Dlta_F_Global=60
        F_REF_Offs=24250.08
        N_REF_Offs=2016667
        F_REF_Range='24250~100000'
    F_REF = F_REF_Offs + Dlta_F_Global*10**(-3)*(N_REF-N_REF_Offs)
    return round(F_REF,6),F_REF_Range



def NR_ARFCN_to_FREQUENCY():
    while True:
        try:
            ARFCN=input("Please input the ARFCN between (0,3279165]:\n")
            ARFCN=int(ARFCN)
            if 0<ARFCN<=3279165:
                NR_Frequency,NR_Frequency_Range=NR_Frequcency_Calculate(ARFCN)
                print("The NR_Frequency of the ARFCN is(MHZ):",NR_Frequency)
                print("It belongs to the Frequency range:",NR_Frequency_Range)
                break
            else:
                print("The input value should be between (0,3279165].Try again!")
        except:
            print("Invalid input,Value should be between (0,3279165],Try again!")

#================================================================================


if __name__=="__main__":
    print('============================================================')
    print('| Welcome to use 5G NR Frequency<-->ARFCN Calculator!       |')
    print('| The Calculator is designed according to 3GPP 38.101-1/2!  |')
#    print('| Author:ZHAO ZHONGXIANG|Contact:10157624@zte.com.cn!     |')

    print('| Author:Kevin|Contact:490359939@qq.com|All rights reserved!|' )
    print('============================================================')
#    print('Attention Please:Make sure your file directory has no Chinese Characters!')

    while True:
        print("------------------------------------------------")
        print("Option 1 for:Frequency-->ARFCN Calculate!")
        print("Option 2 for:ARFCN-->Frequency Calculate!")
        try:
            flag=int((input("Please input your Option(1 or 2):")).strip())
            if flag==1:
                FREQUENCY_to_NR_ARFCN()
                stop_flag=str(input("Do you want to eixt?( y/n):").strip()).upper()
                if stop_flag=='Y':
                    break
            elif flag==2:
                NR_ARFCN_to_FREQUENCY()
                stop_flag=str(input("Do you want to eixt?( y/n):").strip()).upper()
                if stop_flag=='Y':
                    break
            else:
                print("Input Invalid!")
        except:
            print("Input Invalid!")

    input("Press EnterKey to Close the Window!")



# =============================================================================
# #"Calculation of 5G NR ARFCN from 5G NR frequency."
#
# F_REF=float((input("Please input the Centural Frequency(in MHz):\n")).strip())
# #print(F_REF)
#
# if F_REF<0:
#     print("the Frequency should not small than zero!\n" )
#     print("Please Try again!\n")
#     F_REF=float((input("Please input the Centural Frequency(in MHz):\n")).strip())
# elif F_REF<=3000:
#     Dlta_F_Global=5
#     F_REF_Offs=0
#     N_REF_Offs=0
#     N_REF_Range='0~599999'
# elif F_REF<=24250:
#     Dlta_F_Global=15
#     F_REF_Offs=3000
#     N_REF_Offs=600000
#     N_REF_Range='600000~2016666'
# elif F_REF<=100000:
#     Dlta_F_Global=60
#     F_REF_Offs=24250.08
#     N_REF_Offs=2016667
#     N_REF_Range='2016667~3279165'
# else:
#     print("The Frequency is out of band,Please Try again!\n")
#
# N_REF=N_REF_Offs+(F_REF-F_REF_Offs)/(Dlta_F_Global*10**(-3))
# print("The NR_ARFCN of the Frequency is:",int(N_REF))
# print("It belongs to the range:",N_REF_Range)
# =============================================================================




# =============================================================================
# "Calculation of 5G NR frequency from 5G NR ARFCN."
# N_REF=int((input("Please input the Centural NR_ARFCN(in int):\n")).strip())
# #print(F_REF)
#
# if N_REF<0:
#     print("the NR_ARFCN should not small than zero!\n" )
#     print("Please Try again!\n")
#     N_REF=int((input("Please input the NR_ARFCN(in int):\n")).strip())
# elif N_REF<=599999:
#     Dlta_F_Global=5
#     F_REF_Offs=0
#     N_REF_Offs=0
#     F_REF_Range='0~3000'
# elif N_REF<=2016666:
#     Dlta_F_Global=15
#     F_REF_Offs=3000
#     N_REF_Offs=600000
#     F_REF_Range='3000~24250'
# elif N_REF<=3279165:
#     Dlta_F_Global=60
#     F_REF_Offs=24250.08
#     N_REF_Offs=2016667
#     F_REF_Range='24250~100000'
# else:
#     print("The Frequency is out of band,Please Try again!\n")
#
# F_REF = F_REF_Offs + Dlta_F_Global*10**(-3)*(N_REF-N_REF_Offs)
# print("The the Frequency of NR_ARFCN is:",round(F_REF,6)
# print("It belongs to the range:",F_REF_Range)
# =============================================================================



