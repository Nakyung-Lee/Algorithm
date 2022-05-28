from collections import deque
n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(m,x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] >= m and visited[nx][ny] == 0: 
                    visited[nx][ny] = 1
                    queue.append((nx,ny))

cnt = []

arr_min = min(map(min, arr))    
arr_max = max(map(max, arr))   


m = 1
for k in range(arr_min,arr_max+1):
    visited = [[0] * n for _ in range(n)]
    cnt=0
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= k and visited[i][j] == 0:
                bfs(k,i,j)
                cnt+=1
    if cnt > m:
        m = cnt
              
print(m)
