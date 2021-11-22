# 일반적으로 2부터 해당 숫자까지 나누면서 판단하면 시간초과 에러가 난다.
# 그래서 인자로 들어온 수의 제곱근 까지만 확인해도 소수인지 판별이 가능하다는 것을 인지하여 풀었다.
M, N = map(int, input().split())

def is_prime(num): # 소수인지 판단하는 함수
  if num == 1: # 1은 소수가 아니다
    return False # False 반환
  else: # 1이 아닐 경우 
    for i in range(2, int(num**0.5)+1): # 2부터 num의 제곱근까지 
      if num%i == 0: # num으로 나누어 떨어지면 소수가 아니다
        return False
    return True # 2부터 num의 제곱근까지 나눴을 때 나누어떨어지지 않는다면 num은 소수이다.

for i in range(M, N+1):
  if is_prime(i): # True -> 소수
    print(i)