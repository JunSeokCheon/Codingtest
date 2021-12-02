# 주사위를 1부터 6까지 모두 사용할 수도 있는 경우의 수를 구하는 문제이기 때문에 bfs를 사용한다.
# 사다리와 뱀은 동시에 있을 수 없기 때문에 하나의 graph에 표현 가능하다.
# 이 문제의 핵심은 사다리와 뱀을 어떻게 처리할 것인가 인데 필자는 dictionary로 x값을 주면 y값이 나오도록 구현했다.
from collections import deque

n, m = map(int, input().split())
graph = {} # dict 사용
visited = [-1] * 101 # 주사위를 굴린 횟수를 저장

for _ in range(n+m):
  a, b = map(int, input().split())
  graph[a] = b # 주사위나 뱀이나 a값이 오면 b값으로 이동

q = deque()
q.append(1) # 1번칸을 초기값
visited[1] = 0 # 1번칸은 주사위를 굴리기 전 초기 값이기 때문에 0회
while q:
  now_site = q.popleft() # popleft를 하면서 현재 위치를 추출
  for dice in range(1,7): # 주사위 1-6까지 가능한 경우의 수를 for문 처리
    next_site = now_site + dice # 현재 위치와 주사위 수를 더한 값을 다음 위치에 저장
    if next_site > 100: # 다음 위치가 100이 넘어가면 게임의 판을 초과하기 때문에 break
      break
    if next_site in graph: # 만약 다음 위치가 주사위나 뱀의 위치에 있을 때 
      next_site = graph[next_site] # dict의 key에 맞게 value값을 다음 위치로 변경
    if visited[next_site] == -1: # 다음 위치가 아직 가지 않았던 곳이라면
      visited[next_site] = visited[now_site] + 1 # 현재의 주사위 굴린 횟수 + 1
      q.append(next_site) # 다음 위치를 q에 저장

print(visited[100]) # visited는 1-100까지 가는데 주사위 굴린 횟수가 저장