# 필자는 이 문제를 보자마자 deque의 rotate가 생각이 나서 deque를 사용해서 풀었다. why deque ? 원을 이룬다 -> rotate
# deque의 rotate함수는 말그대로 회전하는 기능을 갖는 함수이다. 함수 값이 양수면 오른쪽, 음수면 왼쪽으로 rotate한다.
# N의 크기만큼 1-N 까지 deque에 받아온다.
# que의 맨 앞(=rotate(K-1))으로 K번째 수를 이동하고 제거해준다.
# 그리고 마지막 수인 경우 ","를 출력해주지 않기 때문에 따로 조건문을 둬서 처리해준다.
from collections import deque

N, K = map(int, input().split())
que = deque()

for i in range(1,N+1):
  que.append(i) # 1-N 까지 que에 append

print("<", end="")
while len(que) != 0: # que의 크기가 0일 될 때까지
  que.rotate(-(K-1)) # k번째 수가 맨 앞으로 rotate
  print(que.popleft(), end=", ") # 제거하는 동시에 출력(구분자 "," 생각하면서)
  if len(que) == 1: # 마지막 원소의 경우 ","를 포함하지 않기 때문에 빼준다.
    print(que.popleft(), end="")
print(">", end="")