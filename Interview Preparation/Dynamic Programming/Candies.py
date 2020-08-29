#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    candy = [1]*n
    #print(candy)
    for i in range(n-1):
        if arr[i+1] > arr[i]:
            candy[i+1] = candy[i] + 1
    for i in range(n-1 , 0 , -1):
        if arr[i-1] > arr[i] and candy[i-1]<=candy[i]:
            candy[i-1] = candy[i] + 1
       
    #print(candy)

    return sum(candy)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
