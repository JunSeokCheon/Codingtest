# 가장 작은 or 가장 짧은 or 가장 빠른하면 bfs를 생각하자(deque)
# list.index(value) 하면 value에 맞는 인덱스가 나온다. 

from collections import deque

def bfs(i): 
  visited = [0] * (n+1) # 첫번째 사람부터 n번째 사람까지 visited가 다르기 때문에 사람마다 visited를 다르게 설정해주기 위해 함수안에 선언
  q = deque()
  q.append(i)
  visited[i] = 1 # i번째 사람은 시작이니깐 1로 설정

  while q:
    x = q.popleft()
    for v in graph[x]: # 연결되어 있는 노드들을 하나씩 방문한다.
      if visited[v] == 0: # v를 방문하지 않았다면
        visited[v] = visited[x] + 1 # 1칸 건너일때마다 1씩 증가
        q.append(v) # q에 추가
  
  return sum(visited) # i번째 사람의 케빈 베이컨의 수의 합

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
result = []

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(1,n+1):
  result.append(bfs(i)) # result에 첫 번째~ n번 째 사람까지의 케빈 베이컨의 수의 합이 저장

print(result.index(min(result))+1) # 수가 가장 작은 사람의 인덱스를 뽑고 몇 번째 인지 알기 위해서 +1을 해준다.