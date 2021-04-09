# 큰 수의 법칙
# N, M, K를 공백으로 구분하여 입력받기(개수, 총 횟수, 중복 횟수)
n, m, k = list(map(int, input().split()))
# N 개의 데이터를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬하기
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두번째로 큰 수

result = 0

while True:
    for i in range(k): # 가장 큰 수를 k 번 더하기
        if m == 0: # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 # 더할때마다 1씩 빼기
    if m == 0:
        break
    result += second # 두번째로 큰 수 1번 더하기
    m -= 1

print(result)