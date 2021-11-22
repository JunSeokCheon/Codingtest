# 이 문제는 조건을 이해할수 있다면 쉬운 문제이다.
# 모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
# 모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
# 입력의 종료 조건으로 맨 마지막에 점(.)이 들어온다.
while True:
  string = input()
  stack = [] # 스택 초기화

  if string == ".": # 입력의 종료 조건
    break

  for i in string: # 문자열의 문자하나씩 검토
    if i == "(" or i == "[": # 들어온 문자가 ( or [ 일 때
      stack.append(i) # stack에 넣어준다.
    elif i == ")": # 들어온 문자가 ) 일 때
      if len(stack) != 0 and stack[-1] == "(": # stack의 길이가 0이 아니고, 바로 직전의 입력이 ( 일 때
        stack.pop() # 대칭이 되므로 pop
      else: # 대칭이 되지 않으면
        stack.append(")") # stack에 넣어주고 반복문 탈출 -> 이미 대칭이 깨졌으므로 no
        break
    elif i == "]": 
      if len(stack) != 0 and stack[-1] == "[":
        stack.pop()
      else:
        stack.append("]")
        break
  
  if len(stack) != 0: # stack의 길이가 비어있으면 대칭이라는 의미니깐 yes, 0이 아니고 남아있으면 no 출력
    print("no")
  else:
    print("yes")

# if len(stack) != 0 and stack[-1] == "(":
# if len(stack) != 0 and stack[-1] == "[":
# 위 조건문에서 stack[-1] 부분과 len(stack) 부분을 반대로 적으면 list 범위 에러가 발생한다.
# 예를 들면 ) ( 입력이 들어왔을 때 stack이 비어있는데 stack[-1] 을 찾는것은 범위 에러가 발생한다.
# 그래서 stack의 길이를 먼저 비교해서 오류를 방지해준다. (and 문이기 때문에 첫 조건이 틀리면 그 if문을 틀림.) 
      