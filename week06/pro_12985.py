def solution(n,a,b):
    rnd = 0
    while b!=a:
        rnd += 1
        a,b = (a+1)//2, (b+1)//2 # 반올림 효과
    
    return rnd
