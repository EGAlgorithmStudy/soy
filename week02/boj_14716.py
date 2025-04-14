from collections import deque


def totalLang(M,N,map_grid):
    total_lang = 0
    que = deque()
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    def dfs():
        while que:
            x,y = que.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < M and 0 <= ny < N and map_grid[nx][ny] == 1:
                    map_grid[nx][ny] = 0
                    que.append((nx,ny))
                    
    for i in range(M):
        for j in range(N):
            if map_grid[i][j] == 1:
                que.append((i,j))
                dfs()
                total_lang += 1

    return total_lang

M, N = map(int, input().split())
map_grid = [list(map(int, input().split())) for _ in range(M)]

print(totalLang(M,N,map_grid))