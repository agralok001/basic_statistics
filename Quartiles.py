# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 14:05:59 2019

@author: Alok

#calculating first, second and third quatrtiles
"""

# First quartile Middle number between smallest number and median of the dataset
# The second quartile (Q2) is the median of the data. The third quartile (Q3) is the middle value between the median and the highest value of the data set

#Calculating Quartiles without using numpy
from statistics import median
size = int(input())
numbers = list(map(int, input().split()))
x= sorted(numbers)
print(int(median(x[:size//2])))
print(int(median(x)))
print(int(median(x[(size+1)//2:])))
