# 분해합 = 어떤수 + 어떤수의 각 자리 수의 합
# 여기서 구한는건 어떤수를 구하는 것이다!(문제를 잘 이해할 것)
# brute force로 range의 범위를 1부터 N까지 정해도 되지만 실행시간이 오래 걸리는 단점이 있기 때문에 그것을 보완하기 위해 만든 코드이다
# 각 자리의 수의 합의 최대값은 자릿수*9 이기 때문에 최소값은 분해합 - 자릿수*9로 나타낼수 있다.
N = int(input())
min_N = N - 9*len(str(N)) # 어떤수의 최소값
if min_N > 1: # N이 18이하는 min_N이 0이하가 되기 때문에 min_N을 1부터 N까지 범위를 지정해준다.
  min_N
else:
  min_N = 1

for i in range(min_N, N+1):
  check = i + sum(map(int, str(i))) # i = 어떤수, sum() = 어떤수의 각자리 합

  if check == N: # 분해합이 n과 같다면 i(어떤수)를 출력
    print(i)
    break

  if N == i: # n과 어떤수가 같아진다면 즉 분해합이 없다면 0을 출력
    print(0)
    break