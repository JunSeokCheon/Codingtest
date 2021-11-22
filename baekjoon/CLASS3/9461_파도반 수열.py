n = int(input())

for i in range(n):
  m = int(input())
  dp = [1, 1, 1, 2, 2]

  if m > 5:
    for i in range(5, m):
      dp.append(dp[i-1] + dp[i-5])

  print(dp[m-1])