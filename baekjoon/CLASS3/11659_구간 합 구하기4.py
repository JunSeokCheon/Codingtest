# 일반적으로 풀 경우 시간초과가 나온다. 여기서 일반적이라 하면 입력받은 i,j에 따라 리스트에 접근해서 누적합을 경우를 말한다. 
# 이 문제는 접두사 합을 이용해서 푸는 문제인데, 접두사 합(prefix sum)이라 하면 각 원소까지의 누적합을 리스트에 저장해놓는 것이다.
# i,j를 입력받으면 j까지의 누적합과 i-1까지의 누적합을 빼주면 i,j사이 원소의 합을 구할 수 있다.
# 여기서 sum_list에 0을 넣는 이유는 인덱스 값으로 접근보다는 몇 번째로 접근하는게 가시성이 좋아보인다고 판단했고, i-1번째 원소를 접근해야하는데 i가 0일때 list out of range가 나오기 때문이다.

import sys
N, M = map(int, sys.stdin.readline().split())
N_list = list(map(int, sys.stdin.readline().split()))

total_sum = 0
sum_list = [0]
for i in N_list:
  total_sum += i
  sum_list.append(total_sum) # 각 원소의 누적합 저장

for _ in range(M):
  i, j = map(int, sys.stdin.readline().split())
  print(sum_list[j]-sum_list[i-1])