#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 22:42:42 2018

@author: dandelion
"""

from numpy import *
filename='/home/dandelion/文档/python/machinelearninginaction/Ch02/datingTestSet.txt'

fr = open(filename)
numberOfLines = len(fr.readlines())         #get the number of lines in the file
returnMat = zeros((numberOfLines,3))        #prepare matrix to return
classLabelVector = []                       #prepare labels return
fr = open(filename)
index = 0
for line in fr.readlines():
    line = line.strip()
    listFromLine = line.split('\t')
    returnMat[index,:] = listFromLine[0:3]
    classLabelVector.append(int(listFromLine[-1]))
    index += 1
