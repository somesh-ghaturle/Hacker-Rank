#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    numSwaps = 0
    firstElement = a[0]
    lastElement = a[-1]
    while True:
        swap = False
        for i in range(0, len(a) - 1):
            current_index = i + 1
            if a[i]> a[current_index]:
                lowest = a[current_index]
                highest = a[i]
                a[i]= lowest
                a[current_index] = highest
                
                numSwaps += 1
                swap = True
        if not swap:
            
            break
    print('Array is sorted in', numSwaps, 'swaps.')
    print('First Element:', a[0])
    print('Last Element:', a[-1])

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
