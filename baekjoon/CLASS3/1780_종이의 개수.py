# 2630_색종이 만들기와 유사한 유형으로 색종이에서는 N/2로 나눴지만, 이 문제는 3의 배수로 처리해줘야한다. 
import sys

N = int(sys.stdin.readline())
data = []
for _ in range(N):
  data.append(list(map(int, sys.stdin.readline().split())))
  ans = {"-1":0, "0":0, "1":0}

def addOrDivide(row, col, N):
    value = data[row][col]
    for i in range(N):
        for j in range(N):
            if value != data[row + i][col + j]: # 하나라도 다른값이 나왔으면 쪼개준다
                addOrDivide(row, col, N // 3)
                addOrDivide(row, col + N // 3, N // 3)
                addOrDivide(row, col + N * 2 // 3, N // 3)
                addOrDivide(row + N // 3, col, N // 3)
                addOrDivide(row + N // 3, col + N // 3, N // 3)
                addOrDivide(row + N // 3, col + N * 2 // 3, N // 3)
                addOrDivide(row + N * 2 // 3, col, N // 3)
                addOrDivide(row + N * 2 // 3, col + N // 3, N // 3)
                addOrDivide(row + N * 2 // 3, col + N * 2 // 3, N // 3)
                return
    ans[str(value)] += 1

addOrDivide(0, 0, N)
print(ans["-1"])
print(ans["0"])
print(ans["1"])