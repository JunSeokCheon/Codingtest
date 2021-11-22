import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
name_dict = {}
number_dict = {}

for i in range(1,n+1):
  n = sys.stdin.readline().rstrip()
  name_dict[n] = i
  number_dict[i] = n

for _ in range(m):
  t = sys.stdin.readline().rstrip()
  try:
    print(number_dict[int(t)])
  except:
    print(name_dict[t])