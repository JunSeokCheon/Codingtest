word = input()
alphabet = list(range(97, 123)) # 소문자 a~z 아스키 코드

for i in alphabet:
  print(word.find(chr(i)))   # find(찾을 문자, 찾을 시작 위치) 위치를 반환, 없을경우 -1을 리턴  | 아스키 코드 -> 문자(chr), 문자 -> 아스키 코드(ord)