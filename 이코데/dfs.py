def dfs(graph,v,visited):
  #현재 노드 방문처리
    visited[v]=True
    print(v,end=' ')
    #현재 노드와 연결된 다른 노드 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

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
print(graph[1])
dfs(graph,1,visited)
