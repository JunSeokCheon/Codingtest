# 4분면으로 나눠서 r,c좌표가 사분면에 안에 없으면 **2로 더 늘려서 파악한다.
def z(n, x, y):
    global dist
    if x == r and y == c:  # 목표 r,c과 같으면 방문에 걸리는 거리 출력
        print(int(dist))
        exit(0)
    if n == 1: # 1칸만 이동
        dist += 1 
        return
    if not (x <= r < x + n and y <= c < y + n): # 목표 r,c가 조건안에 없다면 더 넓게 파악
        dist += n ** 2 # n이 **구조라서 **2로 늘린다.
        return
    z(n / 2, x, y)  # 4분면으로 분할해서 재귀함수 호출
    z(n / 2, x, y + n / 2)
    z(n / 2, x + n / 2, y)
    z(n / 2, x + n / 2, y + n / 2)


n, r, c = map(int, input().split())
dist = 0
z(2 ** n, 0, 0)