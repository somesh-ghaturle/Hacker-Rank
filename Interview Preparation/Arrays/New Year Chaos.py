#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    ans = 0
    Q = [P-1 for P in q]
    for i,P in enumerate(Q):
        if P - i > 2:
            print("Too chaotic")
            return
        for j in range(max(P-1,0),i):
            if Q[j] > P:
                ans += 1
    print(ans)
    return

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
