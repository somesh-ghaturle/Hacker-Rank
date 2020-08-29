#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    stack = []
    max_r = 0
    for i in range(len(h)):
        if stack and h[i] < stack[0][0]:
            last_pos = 0
            while stack and stack[0][0] >= h[i]:
                stack_item = stack.pop(0)
                last_pos=stack_item[1]
                max_r = max(max_r, stack_item[0] * (i - stack_item[1]))
            stack.insert(0, (h[i], last_pos))   
        elif not stack or h[i] > stack[0][0]:
            stack.insert(0, (h[i],i))
            
    while stack:
        stack_item = stack.pop(0)
        max_r = max(max_r, stack_item[0] * (len(h) - stack_item[1]))
    return max_r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
