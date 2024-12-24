def solution(keyinput, board):
    x, y = 0, 0
    limit_x = (board[0] - 1) // 2
    limit_y = (board[1] - 1) // 2
    
    for key in keyinput:
        if key == "left":
            x -= 1
        elif key == "right":
            x += 1
        elif key == "up":
            y += 1
        elif key == "down":
            y -= 1
        
        x = max(-limit_x, min(x, limit_x))
        y = max(-limit_y, min(y, limit_y))
    
    return [x, y]