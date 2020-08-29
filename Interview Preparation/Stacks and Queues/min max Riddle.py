#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the riddle function below.
def riddle(arr):
    n=len(arr)
    res=[0]*n
    S=[0]*n

    win=[0]
    for i in range(1,n):
        while len(win)>0 and arr[win[-1]]>=arr[i]:
            win.pop()
        if len(win)==0:
            S[i]=i+1-1
        else:
            S[i]=i-win[-1]-1
        win.append(i)

    win=[n-1]
    for i in range(n-2,-1,-1):
        while len(win)>0 and arr[i]<=arr[win[-1]]:
            win.pop()
        if len(win)==0:
            S[i]+=n-1-i
        else:
            S[i]+=win[-1]-i-1
        win.append(i)

    for i in range(n):
        if res[S[i]]<arr[i]:
            res[S[i]]=arr[i]

    for j in range(n-2,-1,-1):
        res[j]=max(res[j],res[j+1])

    return res
    # complete this function

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = riddle(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
