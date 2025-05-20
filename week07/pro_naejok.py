def solution(a, b):
    answer = 0
    
    for value in range(0, len(a)):
        answer += a[value] * b[value]
    
    return answer