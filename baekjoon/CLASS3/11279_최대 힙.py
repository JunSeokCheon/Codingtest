# 최대 힙문제(heapq를 사용하면 쉽게 해결 가능하다)/ heapq에 대한 학습 필요하다.
# pypy3로 제출
import heapq

n = int(input())
num_list = []
for _ in range(n):
  num_list.append(int(input()))

heap = []
heapq.heapify(heap) # 기본 heap 리스트를 리스트 힙으로 만들기
for i in num_list:
  if i == 0 and len(heap) == 0: # 값이 0이고, 배열이 비어있을 때는 0을 출력
    print(0)
  elif i == 0: # 값이 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 제거
    print(abs(heapq.heappop(heap))) # -을 사용하기 때문에 절대값 abs를 사용, 최대힙이기 때문에 heappop을 하면 최대 값이 나온다.
  else:
    heapq.heappush(heap, -i) # heappush를 사용하고, 최대 힙이기 때문에 -을 사용