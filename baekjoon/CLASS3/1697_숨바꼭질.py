# 가장 짧은 or 가장 빠른하면 bfs를 생각하자 -> bfs는 deque를 사용한다.(그냥 que는 비효율적)
# x-1, x+1, x*2로 분기로 나눠지니깐 dfs로 풀 경우 무한루프에 빠질수있다.
# n,k의 값의 최대값이 100,000 인지한다
from collections import deque # deque 선언

MAX = 100000
n, k = map(int, input().split())
visited = [0] * (MAX+1) # max크기만큼 거리를 저장하는 배열 선언

def bfs(n):
  q = deque()
  q.append(n)

  while q:
    x = q.popleft()
    if x == k: # k의 위치를 찾으면
      print(visited[x]) # 횟수를 출력
      break

    for i in (x-1, x+1, x*2): # x-1, x+1, x*2 분기로 입력을 준다.
      if 0<=i<=MAX and visited[i] == 0: # 문제에 맞게 0보다 크고 max보다 작은 경우일때와 방문하지 않았다면
        visited[i] = visited[x] + 1 # 1초 증가하여 저장
        q.append(i) # q에 추가

bfs(n) 
# 5 17이 입력으로 들어왔을 경우
# 5 > 4/6/10(시간:1)) > 3/5/8, 5(방문)/7/12, 9/11/20(시간:2) -> 17일 나올때의 시간을 찾는다.
# 위에서 방문한 거리는 시간이 저장되어 있기 때문에 중복으로 방문하지 않는다.(if 조건문에 의해)