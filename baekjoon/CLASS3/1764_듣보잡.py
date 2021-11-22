import sys

N, M = map(int, sys.stdin.readline().split())
N_list = []
M_list = []
dict1 = dict()
new_list = []

for i in range(N):
  N_list.append(sys.stdin.readline().strip())

for i in range(M):
  M_list.append(sys.stdin.readline().strip())

for i in N_list:
  if i not in dict1:
    dict1[i] = 1
  else:
    dict1[i]+=1

for j in M_list:
  if j in dict1:
    new_list.append(j)
  else:
    continue

print(len(new_list))
new_list.sort()
for i in new_list:
  print(i)