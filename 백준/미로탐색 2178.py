from collections import deque

def bfs(x,y):
    queue = deque([(x,y,1)])
    visited[x][y] = 1
    while queue:
        x,y,distance = queue.popleft()
        if x == n-1 and y == m-1:
            print(distance)
            break
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny, distance + 1))

n,m = map(int,input().split())

# strip | 한글자씩 끊어서 입력받음
graph = [list(map(int, input().strip())) for _ in range(n)]

visited = [[0] * (m+1) for i in range(n+1)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

bfs(0,0)