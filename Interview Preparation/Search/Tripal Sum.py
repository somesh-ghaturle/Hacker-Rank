#!/bin/python3

import math
import os
import random
import re
import sys
import bisect
# Complete the triplets function below.
def triplets(a, b, c):
    a=list(set(a))
    b=list(set(b))
    c=list(set(c))
    a.sort()
    b.sort()
    c.sort()
    ret=0
    for bb in b:
        ret+=bisect.bisect_right(a,bb)*bisect.bisect_right(c,bb)
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
