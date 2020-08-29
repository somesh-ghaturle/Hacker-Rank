#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the freqQuery function below.
def freqQuery(queries):
    freq = Counter()
    cnt = Counter()
    res = []
    
    for q in queries:
        if q[0]==1:
            cnt[freq[q[1]]]-=1
            freq[q[1]]+=1
            cnt[freq[q[1]]]+=1
    
        elif q[0]==2:
            if freq[q[1]]>0:
                cnt[freq[q[1]]]-=1
                freq[q[1]]-=1
                cnt[freq[q[1]]]+=1
    
        else:
            if cnt[q[1]]>0:
                res.append(1)
            else:
                res.append(0)
    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
