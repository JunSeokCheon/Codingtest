# 1일 될때까지 1을 빼주는것과 k로 나눠주는 것으로 가장 최소의 횟수로 수행하라
# ※ 최대한 많이 나누면 횟수가 최소가 될 수 있다.
# n이 k의 배수가 될 때까지 1을 빼주는 것과 n을 k로 나눠주는 과정을 반복하자

n, k = list(map(int, input().split()))
result = 0

# n이 k 이상이라면 계속 나눠주기
while n >= k:
# n이 k에 나누어 떨어지지 않은다면 1을 빼주기
    while n % k != 0:
        n -= 1
        result += 1
    # k로 나누기
    n /= k
    result +=1

while n > 1:
    n -= 1
    result += 1

print(result)

# 문제 n의 범위가 100억 이상의 큰 수의 경우에는 1씩 빼는 것은 효율적이지 못하다
# n이 k의 배수가 되도록 효율적으로 한 번에 빼는 방식으로 작성하는 것을 권장

n, k = list(map(int, input().split()))
result = 0

while True:
    target = (n // k) * k  # 23, 4일 때, target은 20   
    result += (n-target)  # 1을 한번에 1벙씩 빼주는 방식에서 한방에 다 빼줌, n이 k로 나눠질때까지
    n = target
    if n < k:
        break
    result += 1
    n /= k
    
result += (n-1) # n이 k보다 작은 경우 반복문을 탈출했으니 나머지는 1로 빼줄꺼니 1까지 n-1번 빼줘야함
print(result)