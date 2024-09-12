def solution(n):
#    n<a
    a = n+1
    while format(n,'b').count('1') != format(a,'b').count('1'):
        a+=1
    return a