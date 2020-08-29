#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    fmap={}
    f=[]
    for i,price in enumerate(cost):
        remainder=money-price
        if remainder in fmap:
            f=sorted([fmap[remainder],i])
        if not price in fmap:
            fmap[price]=i
    print(f[0]+1,f[1]+1)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
