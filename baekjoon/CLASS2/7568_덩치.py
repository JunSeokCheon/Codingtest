# 입력을 (키, 몸무게) 형태로 입력받아서 리스트에 넣을 수 있는가 ?
# 리스트의 각 원소에 접근하여 비교할수 있는가 ?
import sys

N = int(sys.stdin.readline()) # 시간을 줄이기 위한 입력
p_list = []

for i in range(N):
  x, y = map(int, sys.stdin.readline().split())
  p_list.append((x,y)) # 사람의 덩치를 (x,y)로 입력받아 p_list에 append

for i in range(N): #  비교시작(버블 정렬)
  rank = 1 # rank 1로 초기화
  for j in range(N):
    if i!=j: # 같은 사람을 비교하지 않기 위해서 조건1
      if (p_list[i][0]<p_list[j][0]) and (p_list[i][1]<p_list[j][1]): # 자신보다 비교할 사람이 키, 몸무게(덩치)가 더 크다면 조건2
        rank+=1 # 자신의 랭크가 +1 즉, 더 낮아짐
  print(rank, end=" ") # 입력 순서대로 자신의 랭크가 나옴, end를 이용해 구분자 설정