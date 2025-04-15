# 나이트의 이동 
from collections import deque

# 나이트가 이동할 수 있는 8가지 방향
dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

def bfs(l, start, end):
 
    queue = deque([(start[0], start[1], 0)])  # x,y, 이동 횟수 
    visited = [[False] * l for _ in range(l)]
    visited[start[0]][start[1]] = True 

    while queue:
        x, y, dist = queue.popleft()

        if (x, y) == end: # 도착!
            return dist

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            # 방문 가능 한곳? 
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))

    return -1  # 못가는 케이스

def main():
    T = int(input()) 
    for _ in range(T):
        l = int(input()) 
        start = tuple(map(int, input().split())) 
        end = tuple(map(int, input().split())) 
        
        result = bfs(l, start, end)
        print(result)

main()