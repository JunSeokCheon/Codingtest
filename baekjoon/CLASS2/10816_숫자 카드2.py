# 이 문제는 이분탐색이나 Dictonary로 풀 수 있는데, 필자는 dictonary로 풀 것이다.
# dictonary 사용법과 구조에 대한 이해가 있어야 한다.
# 먼저 상근이가 가지고 있는 숫자 카드와 개수를 dict에 넣는다
# dict에서 key값을 찾아 value를 반환하고, key 값이 없으면 0을 출력한다.
import sys

N = int(sys.stdin.readline()) 
N_list = list(map(int, sys.stdin.readline().split())) # 상근이가 가지고 있는 숫자카드 입력 

dict1 = dict() # dictonary 선언

for i in N_list: # 가지고 있는 숫자카드 1개씩 꺼냄
  if i not in dict1: # dict1안에 숫자카드가 없으면
    dict1[i] = 1 # 초기 값으로 1
  else: # dict안에 있으면
    dict1[i] += 1 # value 값 +1

M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split())) # 상근이가 찾아야 하는 숫자카드 입력

for j in M_list: # 찾아야 하는 숫자카드 1개씩 꺼냄
  if j in dict1: # dict1안에 찾아야 하는 카드가 있으면
    print(dict1[j], end=" ") # 해당 key값에 맞는 value값 출력, 구분자를 띄어쓰기로 선언
  else: # 해당 key값이 없으면 0 출력
    print("0", end=" ")
