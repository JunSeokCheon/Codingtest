# 문제의 핵심은 체스판 시작의 색깔이 흰색인 경우와 검은색인 경우이다.
# 체스판은 흰색과 검은색 번갈아가며 체크무늬를 이뤄야 한다.
# 보드판을 짤라서, 체크무늬가 되도록 색을 고치는 최소값을 찾는 것이다.

N, M = map(int, input().split())
board = []
new = []

for i in range(N):
  board.append(input()) # board에 추가
 
for i in range(N-7): # 8 * 8로 짤라야하기 때문에 행과 열을 N-7 / M-7로 고정시켜줘야 한다.
  for j in range(M-7):
    w = 0
    b = 0
    for k in range(i, i+8): # 체스판을 고정시킨다음 i,j부터 i+8,j+8까지 체크무늬를 확인한다.
      for l in range(j, j+8):
        if (k+l) % 2 == 0: # 현재 행 i와 열 j의 인덱스 합이 짝수이면 시작점의 색깔과 같아야 하고, 다르면 시작점의 색깔과 다르다는 점을 이용한다. 
        # 여기 if문은 시작점의 색깔과 같아야 하는데 다르다면 w(white), b(black)중에 고쳐야 할 곳에 count+1 해준다.
          if board[k][l] != "W":
            w+=1
          if board[k][l] != "B":
            b+=1
        else: # else의 경우 인덱스 합이 홀수인 경우이다. 시작점의 색깔과 다를 때인데 다르지 않는 경우 count+1 해준다.
          if board[k][l] != "W":
            b+=1
          if board[k][l] != "B":
            w+=1
    new.append(w)
    new.append(b)

print(min(new))