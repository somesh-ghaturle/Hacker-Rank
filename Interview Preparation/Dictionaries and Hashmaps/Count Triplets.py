#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the countTriplets function below.
def countTriplets(arr, r):
    left = defaultdict(int) # when a key does not exist, it returns 0 instead of exception
    right = defaultdict(int)
    for n in arr:
        right[n] += 1
    
    ctr = 0
    for n in arr:
        right[n] -= 1
        if n % r == 0:
            ctr += left[n // r] * right[n * r]
        left[n] += 1
    
    return ctr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
