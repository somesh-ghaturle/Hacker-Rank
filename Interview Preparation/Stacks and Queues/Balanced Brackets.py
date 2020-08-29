#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    if len(s) == 0:
        return "NO"
    if len(s) % 2 != 0:
        return "NO"

    d = set([('(', ')'),('{', '}'), ('[', ']')])
    # print(d)
    stack = []
    opening = set('([{')
    closing = set(')]}')
    for el in s:
        if el in opening:
            stack.append(el)
            #print(stack)
        elif el in closing:
            if len(stack) == 0:
                return "NO"
            try:
                if (stack.pop(),el) not in d:
                    return "NO"
            except:
                return "NO"
    return "YES" if stack == [] else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
