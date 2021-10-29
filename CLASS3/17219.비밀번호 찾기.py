import sys

N, M = map(int, sys.stdin.readline().split())
M_list = []
dict1 = dict()

for i in range(N):
  site, password = map(str, sys.stdin.readline().split())
  dict1[site] = password

for i in range(M):
  M_list.append(sys.stdin.readline().strip())

for i in M_list:
  if i in dict1:
    print(dict1[i])