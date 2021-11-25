# 연결 요소의 개수를 구하는 문제이다.
# 예를 들어, 1-3-4 와 2-5-6으로 이뤄진 그래프가 있다면 여기서 연결 요소의 개수는 2개라고 할 수 있다.
# 간단히 dfs나 bfs를 사용하여 해결 가능하다.
import sys
sys.setrecursionlimit(100000) # dfs 사용 시 재귀의 깊이를 더 늘려줘야 한다.(아니면 런타임 오류 발생)

n, m = map(int, sys.stdin.readline().split())
graph = [[]*(n+1) for _ in range(n+1)]
visited = [0] * (n+1)
count = 0

def dfs(v):
  visited[v] = 1
  for i in graph[v]:
    if visited[i] == 0:
      dfs(i)

for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

for j in range(1, n+1):
  if visited[j] == 0:
    dfs(j)
    count+=1

print(count)