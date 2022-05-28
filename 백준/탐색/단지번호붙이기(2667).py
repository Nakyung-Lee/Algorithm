from collections import deque
n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(x,y):
    count = 1
    arr[x][y]=0
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny]==1: 
                    arr[nx][ny]=0
                    queue.append((nx,ny))
                    count+=1
    return count

cnt = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            cnt.append(bfs(i,j))


cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])
