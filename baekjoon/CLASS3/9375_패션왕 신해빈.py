n = int(input())

for _ in range(n):
  m = int(input())
  dict1 = {}

  for _ in range(m):
    cloth, cloth_type = input().split()

    if cloth_type in dict1:
      dict1[cloth_type] +=1
    else:
      dict1[cloth_type] = 1

  cnt = 1
  for i in dict1.keys():
    cnt = cnt * (dict1[i]+1)

  print(cnt-1)