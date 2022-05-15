import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    # 목적지에 도착했으면 1을 리턴하여 목적지까지 이동한 칸 모든 칸에 1을 더한다.
    if x == 0 and y == 0:
        return 1
    
    # 탐색하지 않은 곳이라면 탐색
    if dp[x][y] == -1:
        dp[x][y] = 0
        
        # 상/하/좌/우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 내에 있고 현재 높이보다 낮은 높이라면
            if 0 <= nx < m and 0 <= ny < n:
                if s[x][y] < s[nx][ny]:
                    # (x, y)칸까지 몇번 이동하는지
                    dp[x][y] += dfs(nx, ny)
                    
    return dp[x][y]


m, n = map(int, input().split())

s = [list(map(int, input().split())) for i in range(m)]

dp = [[-1] * n for i in range(m)]

print(dfs(m - 1, n - 1))
