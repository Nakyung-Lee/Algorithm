from collections import deque

n = int(input())
m = int(input())

graph = [[0] * (n+1) for i in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def bfs(v):
    count = 0
    queue = deque()
    queue.append(v)
    visited[v] = 1
    while queue:
        v = queue.popleft()
        count += 1
        for i in range(1, n+1):
            if graph[v][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1
    return count

print(bfs(1)-1)