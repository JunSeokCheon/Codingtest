# 첫 시도는 문자열 슬라이싱으로 해결하는데 복잡해서 고민하다가 deque으로 구현하면 쉽다고 판단
# R이 들어올때마다 reverse를 해주면 시간초과 -> 그럼 어떻게 ?
# R의 횟수를 저장하여 홀수로 들어오면 pop을 해주고 마지막에 reverse를 해준다. R의 횟수가 짝수면 popleft만 해주고 그대로 출력해주면 된다. (deque 사용)
from collections import deque

t = int(input())

for _ in range(t):
  p = input()
  n = int(input())
  x = input()[1:-1].split(",") # ,기준으로 양 []을 제거하여 x에 저장
  q = deque(x) # x를 deque로 저장

  flag = 0 # 뒤집기(R) 횟수 저장

  if n == 0: # 배열에 들어있는 수가 0일 때 빈 배열로 초기화
    q = []

  for i in p: 
    if i == "R": # R이면 뒤집기 flag 횟수 1증가
      flag += 1
    elif i == "D": # D이고 비어있는 q이면 error 발생
      if len(q) == 0:
        print("error")
        break 
      else: # D이고 비어있지 않는 q이고 뒤집기 횟수가 짝수면 원래 q랑 같기 때문에 popleft
        if flag % 2 == 0:
          q.popleft()
        else: # 뒤집기 횟수가 홀수면 reverse 한다는 의미이기 때문에 pop
          q.pop()
  
  else: # 배열에 들어있는 수가 0이 아니면 원소가 들어있다는 의미
    if flag % 2 == 0: # 뒤집기 횟수가 짝수면 원래 q랑 같으니깐 그대로 출력
      print("["+",".join(q)+"]") # 양쪽 [] 과 join 함수를 사용해 ,를 기준으로 문자열 처리해준 뒤 출력해준다.
    else: # 뒤집기 횟수가 홀수면 한번 뒤집어야 하니깐 reverse 후 출력
      q.reverse()
      print("["+",".join(q)+"]")