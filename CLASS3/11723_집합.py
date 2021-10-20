import sys

N = int(input())
s = set()

for _ in range(N):
  tmp = sys.stdin.readline().split()

  if len(tmp) == 1:
    if tmp[0] == "all":
      s = set([i for i in range(1,21)])
    else:
      s = set()
  else:
    command, target = tmp[0], tmp[1]
    target = int(target)

    if command == "add":
      s.add(target)
    elif command == "remove":
      s.discard(target)
    elif command == "check":
      if target in s:
        print(1)
      else:
        print(0)
    elif command == "toggle":
      if target in s:
        s.discard(target)
      else:
        s.add(target)