# 1012 유기농 배추와 매우 유사한 문제이다. 인접하다는 것은 상하좌우를 고려한다는 의미
from collections import deque

n, m = map(int, input().split())
miro = [list(map(int,input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx = [-1, 1, 0 ,0] # 좌,우
dy = [0, 0, -1, 1] # 상,하

def bfs(x,y):
  q = deque()
  q.append((x,y))
  visited[x][y] = 1 # 0,0부터 시작
  while q:
    a, b = q.popleft()

    if a == n-1 and b == m-1: # 0부터 시작하기 때문에 목표는 n-1과 m-1까지
      print(visited[a][b])
      return
    
    for i in range(4): # 인접한 부분 찾기
      na = a+dx[i]  
      nb = b+dy[i]

      if 0<=na<n and 0<=nb<m: # 0부터 m-1까지
        if visited[na][nb] == 0 and miro[na][nb] == 1: # 방문하지 않았고, 방문해야 하는 곳일때 
          visited[na][nb] = visited[a][b] + 1 # 이동해야 할 칸 수 +1
          q.append((na,nb))

bfs(0,0)