#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    pairs = 0
    arr = sorted(arr)
    i = 0
    j = 1

    while j < len(arr):
        diff = arr[j] - arr[i]
        if diff == k:
            pairs += 1
            j += 1
        elif diff > k:
            i += 1
        else:       # diff < k
            j += 1
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
