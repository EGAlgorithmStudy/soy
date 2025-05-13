from collections import Counter
from itertools import *

def solution(k, tangerine):
    answer = 1
    counter = Counter(tangerine)
    values = sorted(list(counter.values()))
    value_size = len(values)

    max_sum = 0
    for i in range(value_size - 1, -1, -1): 
        max_sum+=values[i]
        if max_sum >=k:
            return answer
        answer += 1


    return answer
