#!/usr/bin/python3
# -*- coding:utf-8 -*-

while True:
	try:
		n=int(input("请输入次数："))
		i=0
		while i<n:
			print(i)
			i+=1
		break
	except:
		print("Invalid input!")
	finally:
		print("please try again!")
input("Press Enter kay to exit!")
