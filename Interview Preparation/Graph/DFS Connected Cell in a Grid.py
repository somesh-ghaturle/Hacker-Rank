#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxRegion function below.
def getMaxRegion(grid,row,column):
    if row<0 or column<0 or row >=len(grid) or column>=len(grid[row]):
        return 0
    
    if grid[row][column]==0:
        return 0

    size=1
    grid[row][column]=0
    for r in range(row-1,row+2):
        for c in range(column-1,column+2):
            if r != row or c !=column:
                size+=getMaxRegion(grid,r,c)
    
    return size


    

# Complete the maxRegion function below.
def maxRegion(grid):
    maxRegion=0

    for row in range(0,len(grid)):
        for column in range(0,len(grid[row])):
            if grid[row][column]==1:
                size=getMaxRegion(grid,row,column)
                maxRegion=max(size,maxRegion)

    return maxRegion

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
