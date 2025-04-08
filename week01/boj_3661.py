def is_valid(sequence, new_num):
    sequence.append(new_num)
    n = len(sequence)

    for i in range(1, n//2 + 1): # 범위는 end를 포함하지않음. 그러므로 +1 해준다.
        if sequence[-i:] == sequence[-2*i:-i]:
            sequence.pop()
            return False
    return True

def find_min_sequence(n):
    sequence = []
    
    def backtrack():
        if len(sequence) == n:
            return True
            
        for num in range(1, 4):
            if is_valid(sequence, num):
                if backtrack():
                    return True
                sequence.pop()
        return False
    
    if backtrack():
        return ''.join(map(str, sequence))
    return "-1"

n = int(input())
print(find_min_sequence(n))