# 문자열 안에 특정 패턴의 문자열이 몇 개 들어가 있는지 확인하는 문자열 문제이다.
# 전체를 돌면서 입력 패턴에 대한걸 찾으면 for문을 2번 써야하기 때문에 시간초과가 난다.
# 그래서 반복문을 하나만 사용하고 쓰는 방법이 요구된다.
# 반복되는 패턴은 IOI 패턴이거 이 패턴이 입력받는 N값과 같다면 포함되어있다고 볼 수 있다.
n = int(input())
m = int(input())
s = input()

result = 0 # 최종 결과 값(몇 번 나오는지)
pattern = 0 # 문제에서 Pn을 찾는 방법(IOI패턴이 몇 번 반복되었는지))
i = 1 # i-1 인덱스부터 점검해야 하기 때문에 1로 초기 값

while i < m-1: # i+1까지 보기 때문에 m-1까지 반복문 실행
  if s[i-1] == "I" and s[i] == "O" and s[i+1] == "I": # i-1, i, i+1 인덱스 값이 "IOI"일 경우
    pattern+=1 # IOI 패턴 1번
    if pattern == n: # 패턴 횟수가 N과 같다면
      pattern -= 1 # pattern 값을 -1해준다. 왜냐하면 목표하는 패턴이 중복으로 나올 경우 때문이다. 한가지의 패턴만 더 찾으면 목표하는 패턴이 되기때문에 -1해줘야 한다.
      result += 1 # S 문자열에 1번 나왔다는 걸 증명
    i+=2 # "IOI"인 경우 "IOIOI" 패턴을 찾기 위해서 i+1이 아닌 i+2 증가
  else: # "IOI"패턴이 아닌 경우
    pattern = 0 # 패턴 0으로 초기화
    i+=1 # i를 1씩 증가하면서 찾기

print(result)