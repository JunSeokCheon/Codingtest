# 완전 탐색으로 하면 시간 초과가 나는 문제이다. 다른 방법이 강구된다.
# 규칙을 찾아보자. 정답을 i라고 가정하면 i-x에 m을 나누면 나머지가 0이다. 마찬가지로 i-y에 n을 나누면 나머지가 0이다.
# 즉, 정답 i는 x,y에 m,n을 계속 더한 값중 하나이다.
# x에 m을 계속 더해준 값에 y를 빼고 n으로 나눈 나머지가 0이라면 그 값이 i값이 될 것이다. 
t = int(input())

def kaing(m,n,x,y):
  while x <= m*n: # 해당 범위를 넘어갈 때까지 없다면 -1 반환
    if (x-y) % n == 0: # i는 x에 m을 계속 더해준 값이니 규칙에 따르면 그 값에 y를 빼고 n으로 나눈 나머지가 0이면 i라고 증명 가능하다.
      return x
    x+=m # x에 m을 계속 더해줌
  return -1

for _ in range(t):
  m, n, x, y = map(int, input().split())
  print(kaing(m,n,x,y))