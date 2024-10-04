def solution(n):
    # n x n 배열을 0으로 초기화
    array = [[0] * n for _ in range(n)]
    
    # 시계 방향으로 이동하기 위한 방향 벡터 (오른쪽, 아래, 왼쪽, 위)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    row, col = 0, 0  # 시작 위치
    direction_index = 0  # 현재 방향 인덱스
    for num in range(1, n * n + 1):
        array[row][col] = num  # 현재 위치에 숫자 배치
        
        # 다음 위치 계산
        next_row = row + directions[direction_index][0]
        next_col = col + directions[direction_index][1]
        
        # 다음 위치가 배열의 범위를 벗어나거나 이미 숫자가 배치된 경우 방향 전환
        if (0 <= next_row < n and 0 <= next_col < n and array[next_row][next_col] == 0):
            row, col = next_row, next_col  # 유효한 위치로 이동
        else:
            # 방향 전환
            direction_index = (direction_index + 1) % 4
            row += directions[direction_index][0]
            col += directions[direction_index][1]
    
    return array

## 미친... 내가 푼거 아님