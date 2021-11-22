# 이 문제의 핵심은 중요도가 같은 문서의 처리를 어떻게 하는지가 관건이다.
# 입력을 보면 첫 줄에 테스트 케이스의 수와 다음 줄에 문서의 개수를 나타내는 N변수와 M번째 문서의 인덱스가 나타난다.
# 그 다음 줄에는 N개 문서의 중요도가 나타난다.
# 출력에는 M번째 문서의 인덱스가 몇 번째로 출력되는지 출력하는 것이다.
# 중요도가 같은 문서가 없다고 가정하면 중요도가 가장 큰 값과 pop(0) 한 값을 찾아서 번째를 출력해주면 되지만 여기서는 중요도가 같은 문서가 존재한다.
# 그래서 인덱스도 저장하는 idx 리스트도 추가하여 처리해준다. 즉, 최대값인지 확인하고 인덱스도 사전에 표시한 값과 맞는지 확인한다.
T = int(input())

for i in range(T):
  N, M = map(int, input().split())
  N_list = list(map(int, input().split()))
  idx = list(range(len(N_list))) # 인덱스 리스트 선언(N_list 길이만큼))
  idx[M] = "target" # 목표 인덱스에 "target"이라고 표시

  order = 0 # 순서 초기화

  while True:
    if N_list[0] == max(N_list): # N_list(중요도 리스트)의 첫 원소가 중요도가 가장 높은 원소일 경우
      order += 1 # 출력 순서 +1

      if idx[0] == "target": # 인덱스 첫 원소가 target일 때
        print(order) # 출력 순서 출력 후 종료
        break
      else: # 인덱스 첫 원소가 target이 아닐 때(중요도가 가장 높은 원소지만 인덱스가 target이 아니면 이제는 필요없기 때문에 삭제해준다.)
        N_list.pop(0) # 중요도 첫 원소 삭제
        idx.pop(0) # 인덱스 첫 원소 삭제

    else: # 중요도가 가장 높은 원소가 아닐 경우
      N_list.append(N_list.pop(0)) # 중요도 첫 원소를 제일 뒤에 붙여준다.
      idx.append(idx.pop(0)) # 첫 인덱스를 제일 뒤에 붙여준다.