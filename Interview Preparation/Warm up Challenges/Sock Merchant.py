#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict 

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairfound = 0
    ar.sort()
    colorDic = defaultdict(int)

    for color in ar:
        colorDic[color] += 1

    for pairs in colorDic.values():
        #if pairs // 2 == 0:
            pairfound += pairs // 2
    return pairfound




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()