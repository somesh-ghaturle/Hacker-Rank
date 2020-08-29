#!/bin/python3
from heapq import heappush, heappop


def on_grid(grid, y, x):
    if y >= 0 and y < len(grid):
        if x >= 0 and x < len(grid[0]):
            return True
    return False


def dijkstra(grid, startX, startY):
    source = (startX, startY)
    prev = None
    visited = set()
    tovisit = [(0, source, prev)]
    dist = {}
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            dist[(x, y)] = -1
    while tovisit:
        try:
            d, node, prev = heappop(tovisit)
        except:
            break
        if dist[node] == -1:
            dist[node] = d
        else:
            if d < dist[node]:
                dist[node] = d
        visited.add(node)
        neighbours = [(node[0] - 1, node[1]),
                      (node[0] + 1, node[1]),
                      (node[0], node[1] - 1),
                      (node[0], node[1] + 1)]
        for n in neighbours:
            if on_grid(grid, n[0], n[1]) and grid[n[0]][n[1]] == '.':
                prev_node = node
                next_node = n
                weight = float('inf')
                if not prev:
                    weight = 1
                else:
                    if prev[0] == node[0]:
                        # horizontal
                        if n[0] == node[0]:
                            weight = 0
                        else:
                            weight = 1
                    elif prev[1] == node[1]:
                        # vertical
                        if n[1] == node[1]:
                            weight = 0
                        else:
                            weight = 1
                if next_node not in visited:
                    next_distance = d + weight
                    heappush(tovisit, (next_distance, next_node, prev_node))
    return dist


def minimumMoves(grid, startX, startY, goalX, goalY):
    dist = dijkstra(grid, startX, startY)
    return dist[(goalX, goalY)]


if __name__ == "__main__":
    n = int(input().strip())
    grid = []
    for i in range(n):
        grid.append(list(input().strip()))
    startX, startY, goalX, goalY = input().strip().split(' ')
    startX, startY, goalX, goalY = [int(startX), int(startY), int(goalX), int(goalY)]
    result = minimumMoves(grid, startX, startY, goalX, goalY)
    print(result)
