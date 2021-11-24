# 그리디 알고리즘의 대표적인 유형으로서, 대부분은 입력값에 정렬을 시도한다.
# 중요한 조건 2개로는 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다는 것과 회의의 시작시간과 끝나는 시간이 같을 수도 있다는 것이다.
# 예를 들면, (7,8), (8,8)과 같이 종료시간이 같을 때 , (7,8)을 먼저 선택하면 (8,8)도 선택할 기회가 생기는데 반대의 경우는 (7,8)을 선택할 수 없다. 
# 그래서 시작시간 기준으로 정렬을 수행한 후 끝시간 기준으로 정렬을 수행한다.
# 전체를 돌면서 초기 끝시간보다 크거나 같은 시작시간을 발견하면 횟수를 증가시키고 해당 끝시간을 end_time로 갱신해준다.

N = int(input())
space = []
cnt = 1

for _ in range(N):
  start, end = map(int, input().split())
  space.append([start,end])

space.sort(key = lambda x : (x[0])) # 시작시간으로 정렬 
space.sort(key = lambda x : (x[1])) # 끝시간으로 정렬

end_time = space[0][1] # 초기 끝시간을 end_time이라고 명시
for i in range(1,N): # 전체를 돌면서
  if space[i][0] >= end_time: # end_time보다 시작시간이 크거나 같으면 두 시각이 연결될 수 있다는 의미이므로 
    cnt+=1 # 횟수 증가
    end_time = space[i][1] # 연결된 시각의 끝시간을 end_time로 갱신

print(cnt) 