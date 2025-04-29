def solution(elements):
    answer = [] # 합 배열 
    circle = elements*2
    
    for i,num in enumerate(elements):
        answer.append(num)
        for nexNum in circle[i+1:i+len(elements)]:
            num += nexNum
            answer.append(num)
            
    return len(set(answer))

print(solution([7,9,1,1,4]))