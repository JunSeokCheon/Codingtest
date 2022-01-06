# 이 문제의 핵심의 최대힙과 최소힙을 둘 다 사용하는데, 삽입할 때는 상관 없지만 삭제할 때 최대힙과 최소힙은 조건이 다르기 때문에 동기화가 필요하다 -> i를 사용(투플 비교연산)
# 조건이 다르다는 말을 이해못한다면 최소힙은 최소값을 삭제할 수 있지 최대 값을 바로 삭제할 수는 없다. 그 반대도 마찬가지라는 의미이다.
# 작동 순서
# 테스트 케이스만큼 반복하고 연산의 수만큼 반복하여 연산을 수행한다.
# 삽입 연산인 경우 최대 힙과 최소 힙을 나누어 푸시하고 정수의 여부를 체크한다.
# 제거 연산의 경우 조건문을 통해 최대 힙을 제거할 건지 최소 힙을 제거할 건지 확인한다.
# 최대 힙이나 최소 힙 모두 반복문을 통해 이미 제거된 정수가 있는지 확인하고 있다면 팝하여 제거한다.
# 그 후 최대 힙이나 최소 힙을 팝하여 제거한다.
# 연산이 끝나고 정수가 없다면 "EMPTY"를 출력한다.
# 정수가 있다면 반복문을 통해 최대 힙과 최소 힙 모두 이미 제거된 정수가 있는지 확인하고 팝하여 제거한 후 최대 힙과 최소 힙을 출력한다.
import sys
import heapq

t = int(sys.stdin.readline())

# 테스트 케이스만큼 반복한다.
for _ in range(t):
    k = int(sys.stdin.readline())
    heap_max = []
    heap_min = []
    visited = [False] * k # 각 i 별로의 활성상태를 기록

    # 반복문을 통행 연산을 수행한다.
    for i in range(k):
        a, b = map(str, sys.stdin.readline().split())

        # 삽입 연산
        if a == "I":
            heapq.heappush(heap_max, (-int(b), i)) # 최대 힙
            heapq.heappush(heap_min, (int(b), i)) # 최소 힙
            visited[i] = True # 정수 생성

        # 제거 연산
        else:
            # 최대 힙 제거
            if b == "1":
                # 반복문을 통해 이미 제거 된 정수는 팝하여 제거
                while heap_max and visited[heap_max[0][1]] == False:
                    heapq.heappop(heap_max)

                # 최대 힙이 있으면 최대 힙 제거
                if heap_max:
                    visited[heap_max[0][1]] = False
                    heapq.heappop(heap_max)

            # 최소 힙 제거
            else:
                # 반복문을 통해 이미 제거된 정수는 팝하여 제거
                while heap_min and visited[heap_min[0][1]] == False:
                    heapq.heappop(heap_min)

                # 최소 힙이 있으면 최소 힙 제거
                if heap_min:
                    visited[heap_min[0][1]] = False
                    heapq.heappop(heap_min)

    # 정수가 없다면 "EMPTY" 출력
    if True not in visited:
        print("EMPTY")
    else:
        # 정수가 있다면
        # 연산이 끝난 후 제거 되지 못한 최대 힙과 최소 힙을 팝하여 제거
        while heap_max and visited[heap_max[0][1]] == False:
            heapq.heappop(heap_max)
        while heap_min and visited[heap_min[0][1]] == False:
            heapq.heappop(heap_min)

        # 최대 힙, 최소 힙 출력
        print(-heap_max[0][0], heap_min[0][0])