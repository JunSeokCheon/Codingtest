result = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
n = input()

for i in result:
  if i in n:
    n = n.replace(i, "+")

print(len(n))