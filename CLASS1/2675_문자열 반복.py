n = int(input())

for i in range(n):
  a, b = input().split()
  text = ""          # 리스트로만 생각하지 않기. 문자열 검토
  for j in b:
    text += j*int(a)  # 리스트 = append | 문자열이니깐 += 로 가능
  print(text)