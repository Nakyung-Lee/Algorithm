import sys
#런타임에러 방치
sys.setrecursionlimit(10000)
 
def dfs(x, y):
    #주어진 범위 벗어나면 종료
    if 0 <= x < h and 0 <= y < w:
        #현재 노드 방문 안했다면
        if graph[x][y] == 1:
            #방문 처리 
            graph[x][y] = 2
            #상 하 좌우 대각선 모두 재귀적으로 호충
            dfs(x-1, y-1)
            dfs(x-1, y)
            dfs(x-1, y+1)
            dfs(x, y-1)
            dfs(x, y+1)
            dfs(x+1, y-1)
            dfs(x+1, y)
            dfs(x+1, y+1)
            return True
        return False
 
while True:
  #시간초과 방지
    w, h = map(int, sys.stdin.readline().split())
    if w==0 and h==0:
        break
    graph=[]
    for i in range(h):
        graph.append(list(map(int, sys.stdin.readline().split())))
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == True:
                dfs(i, j)
                cnt += 1
    print(cnt)
