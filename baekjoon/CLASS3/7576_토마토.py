# 2차원 + dfs(deque) -> 간단한 문제
import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

# 방향 지시(x,y -> 상, 하, 좌, 우)
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

q = deque()
for i in range(n):
  for j in range(m):
    if box[i][j] == 1: # 맨 처음 익은 토마토 찾아서 q에 저장
      q.append((i,j,0))

while q:
  x, y, day = q.popleft()

  for i in range(4): # 인접한 곳으로 이동
    ddx = dx[i]+x
    ddy = dy[i]+y
    dday = day + 1

    if 0<=ddx<n and 0<=ddy<m: # 지정 범위에 있고 익지 않은 토마토라면 익은 토마토로 바꾸고 큐에 저장
      if box[ddx][ddy] == 0:
        box[ddx][ddy] = 1
        q.append((ddx,ddy,dday))

for v in range(n): 
  for l in range(m):
    if box[v][l] == 0: # 하나라도 익지 않은 토마토가 있다면 -1 출력
      day = -1
      break

print(day)