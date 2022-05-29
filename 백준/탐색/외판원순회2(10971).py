import sys

N = int(sys.stdin.readline())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

M =100000000

visited=[0 for _ in range(N)]

def dfs(start,i,sumn,cnt):
    global M
    #모든 도시 들렸고 다시 start 도시로 온 경우
    if cnt == N and start == i:
        if M > sumn:
            M = sumn
            return
    for x in range(N):
        if not visited[i] and graph[i][x] > 0:
            #방문 체크
            visited[i] = 1
            sumn += graph[i][x]
            #sumn이 M보다 작은 경우만 탐색
            if sumn <= M:
                #다음 도시로 이동
                dfs(start,x,sumn,cnt+1)
            #방문한 기록과 합 초기화 (재귀)
            visited[i]=0
            sumn-=graph[i][x]
            
def sol():
    for i in range(N):
        dfs(i,i,0,0)

sol()
print(M)


