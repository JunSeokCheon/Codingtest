# 입력받는 숫자는 0부터 10000사이의 숫자만 입력받는다.
import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001 # 0으로 가득차있는 10001개인 리스트를 생성한다. 

for i in range(n):
  m = int(sys.stdin.readline().rstrip())
  num_list[m] = num_list[m] + 1 # 입력받은 수를 인덱스 값으로 하고 1씩 더해준다.

for i in range(10001): # 처음부터 끝까지 for 반복 
  if num_list[i] != 0: # 입력받은 수가 아니면 고려되지 않는 조건
    for j in range(num_list[i]): # 해당 숫자(= 입력받은 값이 몇 번 나왔는가)만큼 
      print(i) # 입력받은 값 출력


# ex)
# n = 6
# m : 2 3 5 7 2 7
# num_list : [ 0 0 2 1 0 1 0 2 0 0 0 0.... ]

# i = 2, 3, 5, 7 일 때 고려됨
# i = 2
# for j in range(2)
#   print(2) -> 2를 두번 출력

# i = 3
# for j in range(1)
#   print(3) -> 3를 한번 출력

# i = 5
# for j in range(1)
#   print(5) -> 5를 한번 출력

# i = 7
# for j in range(2)
#   print(7) -> 7를 두 번 출력

# --> 2 2 3 5 7 7 출력됨