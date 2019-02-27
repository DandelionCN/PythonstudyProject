#!/usr/bin/env python3
# _*_ coding: utf_8 _*_
"""
Created on Sun Jan  20 22:24:00 2019

@author: dandelion

"""

def Get_Score(city_num,rank,weight):
	seg1=0.3*city_num
	seg2=0.7*city_num
	if rank<=seg1:
		Get_Score=100
	elif rank<=seg2:
		Get_Score=(int(seg2)+1-rank)*100/(int(seg2)+1-int(seg1))
	else:
		Get_Score=0
	Get_Score=Get_Score*weight
	return Get_Score


def Get_CurrentKPI_Score(CurrentKPI_Value,Challenge_Value,Target_Value,Full_Score):
	if Challenge_Value>Target_Value:
		if CurrentKPI_Value>=Challenge_Value:
			Get_CurrentKPI_Score=100
		elif CurrentKPI_Value>=Target_Value:
			Get_CurrentKPI_Score=60+(CurrentKPI_Value-Target_Value)/(Challenge_Value-Target_Value)*40
		else:
			Get_CurrentKPI_Score=60*CurrentKPI_Value/Target_Value
	else:
		if CurrentKPI_Value<=Challenge_Value:
			Get_CurrentKPI_Score=100
		elif CurrentKPI_Value<=Target_Value:
			Get_CurrentKPI_Score=60+(CurrentKPI_Value-Target_Value)/(Challenge_Value-Target_Value)*40
		else:
			Get_CurrentKPI_Score=60*Target_Value/CurrentKPI_Value
	Get_CurrentKPI_Score=Get_CurrentKPI_Score*Full_Score/100
	return Get_CurrentKPI_Score						 



if __name__=="__main__":
	rank_score=Get_Score(14,6,1.0)
	#print(rank_score)
	print("Currentcity score is:{:.2f}".format(rank_score))	
	CurrentKPI_Score=Get_CurrentKPI_Score(0.93,0.99,0.90,5)
	print("CurrentKPI score is:{:.2f}".format(CurrentKPI_Score))

