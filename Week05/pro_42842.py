def solution(brown, yellow):
    answer = [];
    total = brown + yellow 
    
    for i in range(1,yellow+1):
        print(i)
        if yellow%i == 0 :
            y = yellow/i +2
            x = i +2
            if(y*x - yellow) == brown :
                answer.append(x)
                answer.append(y)
                break;
    answer.sort(reverse=True)
    
    return answer
