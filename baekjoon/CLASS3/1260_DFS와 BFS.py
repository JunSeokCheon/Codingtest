# DFS, BFS의 기본이 되는 문제다. 
# DFS는 재귀를 주로 사용하는 거 같고, BFS는 큐나 데크를 사용한다.
# 대게 n+1로 주는 이유는 인덱스 처리에 있어서 헷갈리지 않기 위해서이다.
from collections import deque

n, m, v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
visited_dfs = [0] * (n+1) # dfs 방문여부
visited_bfs = [0] * (n+1) # bfs 방문여부

for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = graph[b][a] = 1 # 양방향이고 두 정점이 연결되었다고 표시(1)

def dfs(v):
  visited_dfs[v] = 1 # 방문표시(1)
  print(v, end=" ") # 방문한 정점을 출력(공백을 기준)
  for i in range(n+1):
    if visited_dfs[i] == 0 and graph[v][i] == 1: # 아직 방문하지 않았고 두 정점이 연결되었다면
      dfs(i) # <재귀사용>

def bfs(v):
  q = deque() # <데크사용>
  q.append(v) 
  visited_bfs[v] = 1 # v의 방문표시(1)

  while q: # 큐가 empty가 될 때까지
    v = q.popleft() 
    print(v, end=" ")
    for i in range(n+1):
      if visited_bfs[i] == 0 and graph[v][i] == 1:
        visited_bfs[i] = 1 # i의 방문표시(여기서 v를 제외한 정점들)
        q.append(i) # i를 큐에 저장(꼬리를 무는 식)

dfs(v)
print()
bfs(v)