from collections import Counter

def solution(weights):
    answer = 0
    wei = Counter(weights)
    
    for w in weights:
        answer += (wei[w] * (wei[w]-1)) / 2
        answer += wei[w] * wei[w*(4/3)]
        answer += wei[w] * wei[w*(4/2)]
        answer += wei[w] * wei[w*(3/2)]   
            
    return answer