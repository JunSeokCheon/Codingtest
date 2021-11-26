# 2630_색종이 만들기 문제와 똑같은 문제이다. 
# n은 언제나 2의 제곱수로 이뤄진다.
n = int(input())
image = [list(map(int, input())) for _ in range(n)] # 2차원 배열 선언

def quadtree(x, y, n):
  check = image[x][y]

  for i in range(x, x+n):
    for j in range(y, y+n):
      if check != image[i][j]: # 하나라도 같은 값이 아니라면 재귀 실행
        print("(", end="")
        quadtree(x,y,n//2) # 1사분면
        quadtree(x,y+n//2,n//2) # 2사분면
        quadtree(x+n//2,y,n//2) # 3사분면
        quadtree(x+n//2,y+n//2,n//2) # 4사분면
        print(")", end="")
        return

  if check == 1: # 모두 1이라면
    print("1", end="")
    return
  else:
    print("0", end="")
    return

quadtree(0,0,n)