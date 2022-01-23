from collections import deque

def bfs(graph,start,visited):
  #큐 구현 위해 deque 라이브러리 사용
    queue=deque([start])
    #방문처리
    visited[start]=True
    #큐가 빌 때까지 반복
    while queue:
      #큐에서 하나 원소 뽑아 출력
        v=queue.popleft()
        print(v,end=' ')
        #해당 원소와 연결된, 아직 방문하지 않은 원소들 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

graph=[
    [],
    #1과 연결된 노드
    [2,3,8], 
    #2와 연결된 노드
    [1,7],
    #3과 연결된 노드
    [1,4,5],
    #4와 연결된 노드
    [3,5],
    #5와 연결된 노드
    [3,4],
    #6과 연결된 노드
    [7],
    #7과 연결된 노드
    [2,6,8],
    #8과 연결된 노드
    [1,7]
]

visited=[False]*9

bfs(graph,1,visited)
