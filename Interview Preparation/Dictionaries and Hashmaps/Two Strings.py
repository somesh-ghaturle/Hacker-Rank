#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    char_tracker = {}
     
    for char in s1:
        if char not in char_tracker:
            char_tracker[char] = 1
             
    for char in s2:
         if char in char_tracker:
            char_tracker[char] += 1
    
    print(char_tracker)
    for element in char_tracker.values():
        if element >= 2:
            return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
