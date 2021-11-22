import sys

n = int(sys.stdin.readline())
time_list = list(map(int, sys.stdin.readline().split()))

time_list.sort()
sum_list = []
result = 0

for i in range(n):
  sum_num = 0
  for j in range(i+1):
    sum_num += time_list[j]
  result += sum_num

print(result)