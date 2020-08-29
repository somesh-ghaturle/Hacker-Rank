#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    ct = 0
    cont = []
    for i in  contests:
        if i[1] == 1:
            cont.append(i[0])
        else:
            ct += i[0]
    cont.sort(reverse = True)
    highLuck = cont[:k]
    lowLuck =  cont[k:]
    ct += sum(highLuck) - sum(lowLuck)
    return(ct)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
