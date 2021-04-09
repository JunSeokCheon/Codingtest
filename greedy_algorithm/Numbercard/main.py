n, m = list(map(int, input().split()))

result = 0
# 한 줄씩 입력받아 처리
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    # 작은 것들 중에서 가장 큰 값 찾기
    result =  max(result, min_value)

print(result)

# 2중 반복문 구조를 사용할 경우
n, m = list(map(int, input().split()))

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)