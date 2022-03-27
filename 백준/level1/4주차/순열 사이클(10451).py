from collections import  deque

import sys

sys.setrecursionlimit(10000)
#런타임에러 방지

def dfs(v):
    visited[v] = 1
    i=s[v]
    if visited[i] == 0:
        dfs(i)

#sys.stdin.readline().split()
#시간초과에러 방지
            
n=int(input())
for i in range(n):
    cnt=0
    m=int(input())
    visited = [0] * (m+1)
    
    #s에 곧바로 배열 입력할 때 [0]+ ~~ 
    s=[0]+(list(map(int, sys.stdin.readline().split())))
    
    for i in range(1,m+1):
        if visited[i]==0:
            dfs(i)
            cnt+=1
    print(cnt)
