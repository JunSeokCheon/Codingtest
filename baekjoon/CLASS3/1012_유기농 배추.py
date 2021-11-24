# bfs 풀이(deque)
# 인접한 1들의 모임을 한 구역이라고 가정하면, 구역마다 지렁이가 1마리가 필요하다고 할 수 있다.
# 처음에 그래프의 칸을 돌다가 1을 발견하면 bfs 실행한다
# 1인칸을 bfs 수행하면 0으로 바뀐다. 그 구역은 전부 0으로 변경한다.
# bfs를 수행하면 1->0으로 바뀌니깐, 1인 구역을 찾으면 지렁이가 1마리 필요하다는 걸 알 수 있다.(cnt +1 해준다.)

from collections import deque

dx = [0,0,1,-1]  # x좌표 (좌우)
dy = [1,-1,0,0]  # y좌표 (상하)

t = int(input())

def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0 # (a,b) 좌표에 있는 배추를 0으로 만듬

    while queue:
        x, y = queue.popleft()
        for i in range(4): # 상하좌우 4번 점검(1을 찾는 과정)
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= m: # 문제 조건에 맞지 않을 때
                continue
            if graph[nx][ny] == 1: # 인접한 곳에 배추(1)가 있으면
                graph[nx][ny] = 0 # 0으로 만들고 queue에 추가
                queue.append((nx, ny))
    return

for _ in range(t):
  n, m, k = map(int, input().split())
  graph = [[0]*m for _ in range(n)] # 가로m 세로n 배추 재배지 graph 생성
  cnt = 0

  for _ in range(k):
    x, y = map(int, input().split()) 
    graph[x][y] = 1 # grpah 상 배추가 있는 곳을 1로 설정

  for a in range(n):
    for b in range(m):
      if graph[a][b] == 1: # 배추가 있다면 bfs 실행하고 지렁이가 1마리 추가
        bfs(graph,a,b)
        cnt +=1
  print(cnt)