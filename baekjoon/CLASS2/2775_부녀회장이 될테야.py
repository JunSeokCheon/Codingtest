T = int(input())

for i in range(T):
  k = int(input())
  n = int(input())

  one_floor = [ i for i in range(1, n+1)] # 0층 리스트

  for _ in range(k): # k 층
    for i in range(1, n):
      one_floor[i] += one_floor[i-1] 
  print(one_floor[-1])