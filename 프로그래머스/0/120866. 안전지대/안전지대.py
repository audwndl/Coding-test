def solution(board):
    answer = 0
    n = len(board) # 보드 크기
    mine = [[0]*n for _ in range(n)]
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:  
                mine[i][j] = 1
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n:
                        mine[ni][nj] = 1
                        
    for i in mine:
        answer+=i.count(0)
    return answer