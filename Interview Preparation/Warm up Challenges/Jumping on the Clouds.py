#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    lenc = len(c)
    position = 0
    while position < lenc:
        if position + 2 < lenc - 1:
            if c[position + 2] == 0:
                position = position + 2
            else:
                position = position + 1
        else:
            #end
            position = lenc
        jumps = jumps + 1
    return jumps
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
