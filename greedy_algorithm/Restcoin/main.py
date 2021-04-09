n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for i in coin_types:
    count += n // i  # // 몫 , / 나누기
    n %= i  # % 나머지

print(f"총 동전의 개수는 {count} 입니다.")