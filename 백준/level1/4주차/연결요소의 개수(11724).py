from collections import  deque

import sys

sys.setrecursionlimit(10000)
#런타임에러 방지

def dfs(v):
    visited[v] = 1
    for i in range(1, n+1):
        if graph[v][i] == 1 and visited[i] == 0:
            dfs(i)

#sys.stdin.readline().split()
#시간초과에러 방지
            
n, m = map(int, sys.stdin.readline().split())
graph = [[0] * (n+1) for i in range(n+1)]
visited = [0] * (n+1)


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a]= 1

cnt=0
for i in range(1,n+1):
    if visited[i]==0:
        dfs(i)
        cnt+=1
        
print(cnt)
