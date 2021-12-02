from collections import deque

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
cnt = []
dx = [-1, 1, 0, 0] # 좌, 우
dy = [0, 0, -1, 1] # 상, 하

def bfs(i,j):
  q = deque()
  q.append((i,j))
  count = 1 # 각 단지의 집의 수를 세긴 위한 변수. 매개변수로 넘어왔다는 것은 집이 있는 곳(1)이라는 의미이므로 초기값 1부터 시작.
  graph[i][j] = 0 # 중복으로 방문하지 않기 위해 0으로 설정

  while q:
    x, y = q.popleft()
    for t in range(4): # 상하좌우(인접)로 분리해서 찾음
      nx = x+dx[t]
      ny = y+dy[t]

      if nx < 0 or nx >= n or ny < 0 or ny >= n: # 해당 범위 밖 일때는 논외
        continue
      if graph[nx][ny] == 1: # 집이 있는 곳이면
        graph[nx][ny] = 0 # 중복방문을 하지 않기 위해 0 설정
        count+=1 # 단지의 집의 수 1 증가
        q.append((nx,ny)) # q에 추가
  
  return count

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1: # 집이 있는 곳이라면
      cnt.append(bfs(i,j)) # bfs 실행해서 각 단지의 집의 수를 cnt 리스트에 저장

cnt.sort() # 정렬 후 단지의 수와 각 단지의 집의 수를 출력
print(len(cnt))
for i in cnt:
  print(i)