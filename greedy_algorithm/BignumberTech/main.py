# 큰 수의 법칙에서 반복되는 수열에 대해서 파악을 해야함
# 6 6 6 5  6 6 6 5 -> 반복되는 수열의 길이는 (k+1)
# 수열이 반복되는 횟수 : m / (k+1) -> k를 곱해주면 가장 큰 수가 나오는 횟수
# m이 나누어 떨어지지 않는 상황을 고려하면 m % (k+1) 만큼 가장 큰수가 더해짐

n, m, k = list(map(int, input().split()))
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

# 가장 큰 수가 더해지는 상황
count = int(m/(k+1))*k
count += (m%(k+1)) # 나누어 떨어지지 않았을 때 나머지 큰수를 더해주는 상황

result = 0
result += (count*first)
result += ((m-count) * second)
print(result)
