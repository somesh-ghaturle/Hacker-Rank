#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minTime function below.
def minTime(machines, goal):
    min_day = math.ceil(goal/len(machines)) * min(machines)
    max_day = math.ceil(goal/len(machines)) * max(machines)
    while min_day < max_day:
        tmp = (max_day + min_day) // 2
        if sum(tmp // m for m in machines) >= goal:
            max_day = tmp
        else:
            min_day = tmp +1
    return min_day

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
