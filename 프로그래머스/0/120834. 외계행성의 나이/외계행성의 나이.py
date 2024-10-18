def solution(age):
    return ''.join(chr(97 + int(digit)) for digit in str(age))
