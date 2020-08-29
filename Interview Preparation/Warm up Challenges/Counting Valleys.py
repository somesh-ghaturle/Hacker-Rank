#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleys = 0
    altitudeUnits = 0

    for step in s:
        if step == 'U':
            altitudeUnits += 1
            #valleys += 1
            if altitudeUnits == 0:
                valleys += 1
        else:
            altitudeUnits -= 1
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
