# 최대힙 문제를 풀고오면 쉽게 풀 수 있다
# pypy3로 제출
import heapq

n = int(input())
n_list = []
for _ in range(n):
  n_list.append(int(input()))

heap = []
heapq.heapify(heap)
for i in n_list:
  if i == 0 and len(heap) == 0:
    print(0)
  elif i == 0:
    print(heapq.heappop(heap))
  else:
    heapq.heappush(heap, i) # 최대 힙에서는 push할 때 -i지만 최소 힙은 i를 push 해준다.