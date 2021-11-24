# 양방향 구조인걸 명시하고, dfs or bfs로 풀수있다.(필자는 dfs로 풀 예정이다)
n = int(input())
m = int(input())
graph = [[]*n for _ in range(n+1)]

for _ in range(m):
  a,b = map(int, input().split())
  graph[a].append(b) # 양방향으로 연결된 graph 그리기
  graph[b].append(a)

cnt = 0
visited = [0]*(n+1)
def dfs(start):
  global cnt # 전역변수로 선언하여 반환값으로 반환하지 않아도 됨
  visited[start] = 1 # 1은 바이러스에 걸린 컴퓨터에 포함되지 않기 때문에 1로 만들어줌
  for i in graph[start]: # 그래프에 연결된 애들 하나하나 탐색 
    if visited[i] == 0: # 방문하지 않았던 컴퓨터들만 탐색
      dfs(i) # 재귀를 통해 깊게 들어감
      cnt+=1 # 그래프에 연결되었고, 양방향이기 때문에 중복을 제거한 컴퓨터들은 바이러스에 걸렸기 때문에 +1

dfs(1)
print(cnt)