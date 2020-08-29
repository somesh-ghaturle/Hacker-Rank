  
#!/bin/python3

import os
import sys
from collections import deque
sys.setrecursionlimit(10000)


class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def __inorderUtil(self, temp):
        if not temp:
            return
        self.__inorderUtil(temp.left)
        print(temp.key, end=' ')
        self.__inorderUtil(temp.right)

    def inorder(self):
        self.__inorderUtil(self.root)
        print()
    def getLevels(self):
        levels=[]
        levels.append([self.root])
        i=0
        while(levels[i]):
            next_lev=[]
            for x in levels[i]:
                if x.left:
                    next_lev.append(x.left)
                if x.right:
                    next_lev.append(x.right)
            levels.append(next_lev)
            i+=1
        return levels
                

    def __insertUtil(self,arr):
        arr=arr[::-1]
        self.root=Node(1)
        p=self.root
        q = deque()
        q.appendleft(p)
        while q:
            p=q.pop()
            l,r = arr.pop()
            if l!=-1:
                p.left=Node(l)
                q.appendleft(p.left)
            if r!=-1:
                p.right=Node(r)
                q.appendleft(p.right)

    def insert(self, arr):
       self.__insertUtil(arr)


def swapNodes(indexes, queries):
    t=Tree()
    t.insert(indexes)
    levels=t.getLevels()
    for k in queries:
        for i in range(k,len(levels)+1,k):
            for x in levels[i-1]:
                x.left,x.right=x.right,x.left
        t.inorder()



if __name__ == '__main__':

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)
