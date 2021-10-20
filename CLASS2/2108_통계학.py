# 이 문제에서 산술평균, 중앙값, 범위는 쉽게 풀 수 있어서 따로 풀이는 하지 않고, 최빈값에 대해서만 풀이
# Counter, Counter.most_common에 대해서 알고 있어야 한다.
# 2차원 배열이나 리스트에 대한 이해도가 있어야 한다.
from collections import Counter
import sys

n = int(sys.stdin.readline())
n_list = []

for i in range(n):
  n_list.append(int(sys.stdin.readline()))

n_list.sort() # sort 해주는 이유 : 여러 개 있을 때 2번째로 작은 값을 뽑아줘야 하기 때문에 
tmp = Counter(n_list).most_common() # most_common 을 이용해 n_list에서 빈도가 높은 순으로 전체를 반환 ("항목" : 개수)로 표현.

if len(tmp) > 1: # 항목 개수가 1이상이면 조건1
  if tmp[0][1] == tmp[1][1]: # 제일 큰 최빈값의 개수와 두번째로 큰 최빈값의 개수가 같으면 조건2
    print(tmp[1][0]) # 두 번째 최빈값 항목을 출력
  else: # 개수가 같지않으면
    print(tmp[0][0]) # 첫 번째 가장 큰 최빈값 항목 출력
else: # 항목이 1개라면
  print(tmp[0][0]) # 첫 번째(=최빈값) 항목 출력 

  # Counter는 리스트나 투플, 딕셔너리의 항목들에 대한 개수를 측정하여 ("항목":개수) 형태의 딕셔너리로 반환해주는 함수이다.
  # Counter(n).most_common()은 n에서 빈도가 높은 순으로 전체를 반환한다.