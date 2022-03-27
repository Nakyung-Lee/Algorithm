from collections import deque
import sys
sys.setrecursionlimit(100000)

n=int(input())

def bfs(v):
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if root[i]==0:
                queue.append(i)
                root[i]=v
    return root
    
root=[0]*(n+1)           
graph = [[] for i in range(n+1)]

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
root=bfs(1)
                      
for i in range(2,len(root)):
    print(root[i])
