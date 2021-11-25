# 문제를 이해하기만 하면 쉬운 문제이다.
# Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다 라는 의미는 해당 Xi가 리스트에 몇번째인지 구하는 것이다.(0번째 부터시작)
# list.index로 할 경우 시간초과가 나기때문에 dictionary를 이용해주자
import sys
n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))

n_sort = list(sorted(set(n_list))) # dic을 이용하기 전 정렬을 해주고 중복을 제거해준다.
dic = {n_sort[i]:i for i in range(len(n_sort))} # dic에 n_sort의 key에 0부터 value값을 지정해준다.

for j in n_list:
  print(dic[j], end=" ") # n_list 값을 dic에 넣어줌으로써 순서를 출력해준다.