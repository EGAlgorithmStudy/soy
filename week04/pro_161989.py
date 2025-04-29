def solution(n, m, section):
    section.sort()
    answer = 0
    cur_position = 0 

    for sect in section:
        if sect > cur_position:
            answer = answer + 1 
            cur_position = sect + m - 1

    return answer

n = 8
m = 4
section = [2, 3, 6]
solution(n,m,section)