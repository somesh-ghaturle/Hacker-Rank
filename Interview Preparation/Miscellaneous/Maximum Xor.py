#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxXor function below.
def maxXor(arr, queries):
    # solve here
    ans = []
    maxlen = len(bin(max(arr + queries))) - 2
    #print(maxlen)
    trie = {}
    for number in ['{:b}'.format(a).zfill(maxlen) for a in arr]:
        cur = trie
        for c in number:
            cur = cur.setdefault(c,{})
        #print(trie)
    for q in queries:
        cur = trie
        s = ''
        number = '{:b}'.format(q).zfill(maxlen)
        for c in number:
            bestB = str(int(c) ^ 1)  #if arr can offer bestB, the result will be maximum
            #print(c,bestB) 
            factB = bestB if bestB in cur else c
            s += factB
            cur = cur[factB]
        #print(s)
        ans.append(int(s, 2) ^ q)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    queries = []

    for _ in range(m):
        queries_item = int(input())
        queries.append(queries_item)

    result = maxXor(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
