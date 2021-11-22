a = int(input())
b = int(input())
c = int(input())
multi = list(str(a*b*c))   # 숫자 연산을 list로 만드는 방법은 결과값에 str을 씌워주면 된다!
word = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

for i in word:
  print(multi.count(i))