#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.

# Time out...
# def checkMagazine(magazine, note):
#     flag = True

#     for i in range( len(note)):
#         if note[i] in magazine:
#             magazine.remove(note[i])
#         else:
#             print("No")
#             flag = False
#             break
#     if flag:
#         print("Yes")

def checkMagazine(magazine, note):
    
    if (Counter(note) - Counter(magazine)) == {}:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
