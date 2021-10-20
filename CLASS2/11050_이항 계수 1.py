N, K = map(int, input().split()) 
# 이항 계수 : nCr = n! / k!(n-k)! 공식 이용
def fact(N):
  if N<=1:
    return 1
  else:
    return N * fact(N-1)
print(fact(N) // (fact(K)*fact(N-K)))