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