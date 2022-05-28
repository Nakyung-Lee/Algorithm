from collections import deque
from sys import stdin

n = int(input()) # 컴퓨터의 수
m = int(input()) # 연결된 수


graph = [[0] * (n+1) for _ in range(n+1)] 

for _ in range(m):
    x, y = map(int, stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited = [False] * (n+1) # 감염여부에 대한 리스트 생성 

def bfs(v):
    count = 0  # 감염된 컴퓨터의 수
    queue = deque()
    queue.append(v)
    visited[v] = True # 감염이 되면 True

    while queue:
        v = queue.popleft() 
        count += 1 # pop을 해줄때마다 카운트
        for i in range(len(graph[v])):
            if graph[v][i] == 1 and visited[i] == False:
                queue.append(i)
                visited[i] = True
    return count 

print(bfs(1)-1)
