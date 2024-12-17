def solution(cipher, code):
    answer=""
    jump = code
    while jump <= len(cipher):
        answer += cipher[jump-1]
        jump += code
    return answer