from collections import deque

def elevator(F, S, G, U, D):
    visited = [False] * (F + 1)

    queue = deque([(S, 0)]) # 위치, step
    while queue : 
        current, step = queue.popleft()

        if current == G : 
            return step
        if current + U <= F and not visited[current + U] :
            visited[current + U] = True
            queue.append((current + U, step + 1))
        if current - D >= 1 and not visited[current - D] :
            visited[current - D] = True
            queue.append((current - D, step + 1))

    return "use the stairs"


F, S, G, U, D = map(int, input().split())

print(elevator(F, S, G, U, D))