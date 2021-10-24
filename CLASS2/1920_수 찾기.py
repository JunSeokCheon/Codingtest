# 이 문제는 in 연산자를 이용해 풀수있지만 이분 탐색에 더 익숙해지기 위해서 이분 탐색으로 풀었다.
# 이분 탐색을 사용하기 전에 탐색을 할 자료형에 sort(정렬)해주는 것은 필수이다.
# 이분 탐색 함수를 만들어 찾고자 하는 원소를 하나씩 넣고 True를 반환하면 1을 출력 아니면 0을 출력하도록 구현했다.
import sys

M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))
M_list.sort() # 이분탐색을 위한 정렬
N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))

def binary(num):
  start = 0 
  end = M-1 # M_list 에서 찾기 때문에 크기를 적어준다.(인덱스로 접근하기 위해서 -1 해준다.)

  while start <= end: 
    mid = (start+end) // 2
    if M_list[mid] == num: # M_list의 값이 인자로 넘어온 값과 같으면 원소가 존재한다는 의미
      return True # True 반환해준다.
    
    if M_list[mid] < num: # 찾고자하는 원소보다 M_list[mid]값이 더 작으면
      start = mid + 1 # start 값을 end 쪽으로 땡겨주어 범위를 좁게 한다.
    elif M_list[mid] > num: # 찾고자하는 원소보다 M_list[mid]값이 더 크면
      end = mid - 1 # end 값을 start 쪽으로 땡겨주어 범위를 좁게 한다.

for i in range(N):
  if binary(N_list[i]): # 찾고자 하는 원소 하나씩 함수에 넣어준다.
    print("1")
  else:
    print("0")