import math

n = int(input())
n_factorial = str(math.factorial(n))  # n!
cnt = 0
#  팩토리얼 계산값의 1의 자리부터 처음 0이 아닌 숫자가 나오기까지 0의 개수 카운트
for i in range(len(n_factorial)-1, -1, -1):
    if n_factorial[i] == '0':
        cnt += 1
    else:
        break
print(cnt)