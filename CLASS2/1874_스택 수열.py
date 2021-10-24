# 이 문제는 문제를 잘 읽고 이해를 하는 것이 먼저다. (필자는 문제를 이해하는데 오랜 시간이 걸렸다)
# 1. 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만든다.
# 2. 스택에 push하는 순서는 반드시 오름차순
# 3. 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지
# 스택을 이용해 그 수열을 만드는 지는 스택에 pop을 했을 시 입력한 숫자와 같지 않으면 수열을 만들 수 없다고 가정
# 입력의 첫 줄에 n, 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어짐.
# 출력은 입력된 수열을 만들기 위한 연산을 한 줄에 한 개의 연산 출력
# 예제를 보면 n = 8, 4 3 6 8 7 5 2 1이 나왔는데 위 1번에서 보는 것처럼 cnt 변수를 1부터 4까지 stack append하고 +도 결과 리스트에 저장한다.
# 4는 stack[-1]와 값이 같으니깐 pop과 -를 추가한다. 3도 동일
# cnt를 5, 6 stack append, + 추가 -> 6 pop
# 7,8 stack append -> 8 pop
# 7 -> pop, 5 -> pop, 2 -> pop, 1 -> pop
# flag에 따라 result 출력 or NO 출력
# 숫자와 stack[-1] 값이 다를 경우 수열을 이룰수 없기 때문에 flag : False ->NO 출력
N = int(input())
stack = []
result = []
cnt = 1
flag = True

for i in range(N):
  num = int(input()) # num 정수를 받는다.
 
 while cnt <= num: # cnt가 1부터 num까지 stack append와 +기호를 추가한다.
    stack.append(cnt)
    result.append("+")
    cnt+=1 # cnt 1씩 더해서 추가
  
  if num == stack[-1]: # stack의 최근에 들어온 수와 num과 같으면 pop해주고 -기호 추가
    stack.pop()
    result.append("-")
  else: # 수열 x
    flag = False 
    break

if flag == True: # 수열이 가능하다는 의미이므로 result 기호 출력
  for j in result:
    print(j)
else:
  print("NO")