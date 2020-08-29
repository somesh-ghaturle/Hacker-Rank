#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_road >= c_lib:
        return n*c_lib
    city_connection_map = create_city_connection_map(cities)
    visited_array = [False] * (n+1)
    min_costs = 0
    for i in range(1,n+1):
        if not visited_array[i]:
            roads = bfs(i, city_connection_map, visited_array)
            if roads >= 0:
                min_costs += min(roads*c_road+c_lib, (roads+1)*c_lib)
    return min_costs

def bfs(city, city_connection_map, visited_array):
    queue = []
    queue.append(city)
    roads = -1
    while queue:
        node = queue.pop(0)
        if not visited_array[node]:
            visited_array[node] = True
            roads+=1
            for dest_city in city_connection_map.get(node, []):
                if not visited_array[dest_city]:
                    queue.append(dest_city)
    return roads

def create_city_connection_map(cities):
    city_connection_map = {}
    for connection in cities:
        city_connection_map.setdefault(connection[0],[]).append(connection[1])
        city_connection_map.setdefault(connection[1],[]).append(connection[0])
    return city_connection_map

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
  