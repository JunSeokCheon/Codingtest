# 사전순으로 정렬 후 길이 순으로 정렬하는 것이 핵심이다.
# 두 번 정렬하는데 길이 순으로 정렬하는 방법만 알면 쉬운 문제이다.
# 중복되는 원소를 제거하는 것은 set 집합 함수를 사용하면 간단하다.
# 입력받을 때 rstrip을 쓰는 이유는 sys.stdin.readline() 입력은 개행을 포함하여 입력받기 때문에 제거해줘야 하기 때문이다.
import sys

n = int(sys.stdin.readline())
sort_list = []

for i in range(n):
  sort_list.append(sys.stdin.readline().rstrip())

sort_list = list(set(sort_list))
sort_list.sort()
sort_list.sort(key = lambda x : len(x)) # =sort(key = len)

for j in sort_list:
  print(j)