#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue March 15:30:55 2018

@author: admin """

from tkinter import *
window=Tk()

window.title("欢迎使用Tkinter")


lbl=Label(window,text="Hello")
lbl.grid(column=0,row=0)
window.mainloop()

window.geometry("500×300")

