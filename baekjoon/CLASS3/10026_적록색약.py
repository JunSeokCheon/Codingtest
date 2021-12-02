# dfs, bfs 두가지 방법으로 풀 수 있다. 필자는 bfs로 푸는 것을 좋아한다!
# 일반인의 경우와 적록색약인 사람의 경우 두가지로 나눠서 풀이하면 쉽다.
# dfs 함수에 넣기 전에 적록색약인 사람은 "R"과 "G" 둘다 "R" 로 처리해주면 된다.
# dfs 함수의 인자로 위치(i,j), 해당 그래프, 방문위치 저장하는 리스트를 넘겨준다.
import sys
from collections import deque

def bfs(i,j, block,visited):
  q = deque()
  q.append((i,j))
  visited[i][j] = 1 # i,j 위치에 방문했다고 표시 

  while q:
    x, y = q.popleft()
    for dict in range(4): # 상,하,좌,우 인접한 위치 탐색
      ddx = dx[dict] + x
      ddy = dy[dict] + y

      if 0<=ddx<n and 0<=ddy<n and block[x][y] == block[ddx][ddy] and visited[ddx][ddy] == 0: # ddx,ddy가 만족하는 범위를 넘어가지 않고, (x,y)와 (ddx,ddy)의 색깔이 같고, (ddx,ddy) 방문하지 않은 곳이라면
        visited[ddx][ddy] = 1 # 방문했다고 표시하고
        q.append((ddx,ddy)) # q에 저장


dx = [-1,1,0,0] # 좌,우
dy = [0,0,-1,1] # 상,하

n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline()) for _ in range(n)] # 일반인의 그림
graph_rb = [[0] * n for _ in range(n)] # 적록색약인의 그림
cnt1 = 0
cnt2 = 0

for i in range(n): 
  for j in range(n): 
    if graph[i][j] == "G" or graph[i][j] == "R": # 적록색약의 경우 G,R을 R로 보고, 나머지는 B로 본다
      graph_rb[i][j] = "R"
    else:
      graph_rb[i][j] = "B"

visited1 = [[0] * n for _ in range(n)] # 정상인의 방문 리스트

# 일반인의 경우
for i in range(n):
  for j in range(n):
    if visited1[i][j] == 0: # 방문하지 않았다면
      bfs(i,j,graph,visited1) # BFS 함수 실행
      cnt1+=1 # 구역 증가

visited2 = [[0] * n for _ in range(n)] # 적록색약인의 방문 리스트

# 적록색약의 경우
for i in range(n):
  for j in range(n):
    if visited2[i][j] == 0: # 방문하지 않았다면
      bfs(i,j,graph_rb,visited2) # BFS 함수 실행
      cnt2+=1 # 구역 증가

print(cnt1, cnt2)