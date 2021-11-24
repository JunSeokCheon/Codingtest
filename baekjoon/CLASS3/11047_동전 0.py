# 대표적인 그리디 알고리즘인, 동전 개수 최소개수를 구하는 문제이다.
# 제일 큰 동전부터 나눠주면 되는 쉬운 문제다.
# 필자는 처음 입력받은 k보다 더 큰 동전을 받으면 처음부터 제외했다.
n, k = map(int, input().split())
coin = []
cnt = 0

for _ in range(n): 
  money = int(input())
  if money > k:  # k보다 입력받은 동전의 단위가 크면 coin list에 추가하지 않는다.
    continue
  else:
    coin.append(money)


while k>1: # k가 0이 될 때까지
  for i in range(len(coin)-1, -1, -1): # 역순(큰 동전)으로 접근
    if coin[i] > k: # 나눠지는 동전의 단위가 현재 k값보다 크면 다른 동전 단위로 넘어가게 한다.
      continue
    else:
      count = k // coin[i] # 동전 개수 저장
      k = k % coin[i] # k값 갱신
      cnt += count # 총 개수에 더해줌

print(cnt)