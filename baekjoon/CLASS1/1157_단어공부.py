word = input().upper()
word_overlap = list(set(word)) # set 자료형에 저장된 값을 인덱싱으로 접근하려면 다음과 같이 리스트나 튜플로 변환
maxlist = []

for i in word_overlap:
  maxlist.append(word.count(i))

if maxlist.count(max(maxlist)) > 1:
  print("?")
else:
  print(word_overlap[maxlist.index(max(maxlist))])