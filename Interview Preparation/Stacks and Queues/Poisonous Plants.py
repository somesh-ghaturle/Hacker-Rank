#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the poisonousPlants function below.
def poisonousPlants(p):
    stack = []
    max_day = 0
    for i in range(len(p)):
        plant = p[i]
        mdays = 0
        while stack and stack[-1][0] >= plant:
            other_plant = stack.pop()
            mdays = other_plant[1] if mdays < other_plant[1] else mdays
        mdays = mdays + 1 if stack else 0
        stack.append( (plant, mdays) )
        max_day = max(mdays, max_day)
        
    return max_day
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()
