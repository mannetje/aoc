#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 19:35:49 2020

@author: sido
"""

import numpy as np

filepath = '../input/03/input.txt'
#filepath = '../input/03/example.txt'

#First check needed array size
col_length = 0
row_length = 0
with open(filepath, 'r') as input_text:
    for line in input_text:
        col_length = len(line)-1 if len(line)-1 > col_length else 0 #-1 to strip \n, but why does example NOT have this...?
        row_length += 1

#Create the zeroed array and fill with data
a = np.zeros((row_length, col_length), np.int)
with open(filepath, 'r') as input_text:
    for r in range(0, row_length):    
        line = input_text.readline()
        for c in range(0, col_length):
            if line[c] == '#':
                a[r][c] = 1

print(row_length)
print(col_length)

slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
ans = 1

for s in slopes:
    row = 0
    col = 0
    trees = 0
    for row in range(0, row_length, s[1]):    
        #print (f'row:{row}. col:{col}')
        if row != 0:
            if a[row][col] == 1:
                    trees +=1
            
        if row == row_length-1:        
            #print (a[row])
            break
        for i in range(0, s[0]):
            col += 1        
            if col >= col_length:
                col = 0                                    
        #print (a[row])
    print (f'Total trees is {trees}')
    ans *= trees
    
print (f'Answer is {ans}')


