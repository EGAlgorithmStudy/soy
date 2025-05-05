def solution(citations):
    answer = 0   
    citations.sort(reverse=True)
    
    for idx, i in enumerate(citations, start = 1):     
        answer = max(answer, min(i, idx))
    
    return answer
