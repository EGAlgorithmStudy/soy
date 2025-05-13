def solution(s):
    count = 0
    deleted_zero = 0 # 지운 0의 수 

    while s != "1":
        count += 1
        num = len(s)
        s = s.count("1")*"1"
        deleted_zero += num - len(s)
        s = len(s)
        s = bin(s)[2:]

    return [count,deleted_zero]
