#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * (n + 1)
    for i in queries:
        arr[i[0]] += i[2]
        if i[1] < n:
            arr[i[1] + 1] -= i[2]

    x = 0
    max1 = 0
    for i in range(1, n + 1):
        x += arr[i]
        if x > max1:
            max1 = x
    return max1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
