# 처음부터 오를 생각보다는 결국 마지막 계단은 올라야하니깐 마지막 계단을 밟았다고 가정한다.
# 그러면 마지막 계단 전에서 올라온 경우와, 마지막 계단 전전에서 올라온 경우가 있다.
# 그런데 전자의 경우에는 3칸 연속 밟을 수 있기 때문에, 마지막과 마지막 전 계단은 밟았다고 가정하고 풀이한다.
import sys

n = int(sys.stdin.readline())
num_arr = []
dp = []

for _ in range(n):
  num_arr.append(int(input()))

if n == 1:
  dp.append(num_arr[0])
elif n == 2:
  dp.append(num_arr[0])
  dp.append(max(num_arr[1], num_arr[0] + num_arr[1]))
else:
  dp.append(num_arr[0])
  dp.append(max(num_arr[1], num_arr[0] + num_arr[1]))
  dp.append(max(num_arr[0]+num_arr[2], num_arr[1]+num_arr[2]))
  for i in range(3, n): 
    dp.append(max(dp[i-2]+num_arr[i], dp[i-3]+num_arr[i-1]+num_arr[i]))

print(dp[-1])