#!/bin/python3

import math
import os
import random
import re
import sys

def findCapital(capitals, cityId):
    capitalId = capitals[cityId][0]
    if capitalId == cityId:
        return capitalId
    return findCapital(capitals, capitalId)

def union(capitals, capitalId1, capitalId2):
    capitals[capitalId1][0] = capitalId2
    return capitals

def removeRoads(roads, capitals):
    totalTime = 0
    for road in roads:
        city1 = road[0]
        city2 = road[1]
        cost = road[2]
        capitalId1 = findCapital(capitals, city1)
        capitalId2 = findCapital(capitals, city2)
        # If both cities have machine occupied capitals, remove that road
        # Otherwise, merge the two cities
        if capitals[capitalId1][1]:
            if capitals[capitalId2][1]: 
                if capitalId1 != capitalId2:
                    totalTime += cost
            else:
                capitals = union(capitals, capitalId2, capitalId1)
        else:
            capitals = union(capitals, capitalId1, capitalId2)
    return totalTime

def minTime(roads, machines):
    # A list of capitals. index=cityId, value=[capitalId, hasMachine]
    capitals = [[i, False] for i in range(n)]
    for machine in machines:
        capitals[machine][1] = True
    # Sort the roads by cost in decreasing order so the more pricy road is omitted first
    roads.sort(key=lambda x:x[2], reverse=True)
    totalTime = removeRoads(roads, capitals)
    return totalTime

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    roads = []
    skip = False
    try:
        for _ in range(n - 1):
            roads.append(list(map(int, input().rstrip().split())))
    except:
        roads = [[0,3,3],[1,4,4],[1,3,4],[0,2,5]]
        k = 3
    machines = []
    try:
        for _ in range(k):    
            machines_item = int(input())
            machines.append(machines_item)
    except:
        machines = [1,3,4]
    result = minTime(roads, machines)
    fptr.write(str(result) + '\n')
    fptr.close()
