def fibon(num):
  zero_count = [1,0]
  one_count = [0,1]

  if num <= 1:
    return

  for i in range(2,num+1):
    zero_count.append(zero_count[i-1]+zero_count[i-2])
    one_count.append(one_count[i-1]+one_count[i-2])

  return zero_count, one_count

T = int(input())
zero_count, one_count = fibon(40)

for _ in range(T):
  m = int(input())
  print(zero_count[m], one_count[m])