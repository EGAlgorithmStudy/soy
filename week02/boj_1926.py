
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def find_picture(N,M, map_grid):
    visited = [[False] * M for _ in range(N)]
    picture_count = 0
    max_size = 0

    def dfs(x,y):
        visited[x][y] = True
        stack = [(x,y)]     
        size = 1

        while stack:
            x,y = stack.pop()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and map_grid[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    stack.append((nx,ny))
                    size += 1
        return size
    
    for i in range(N):
        for j in range(M):
            if map_grid[i][j] == 1 and not visited[i][j]:
                picture_count += 1
                max_size = max(max_size, dfs(i,j))

    print(picture_count)
    print(max_size)
    



N, M = map(int, input().split())
map_grid = [list(map(int, input().split())) for _ in range(N)]    

# 그림 개수, 가장 넓은 그림의 크기 출력
find_picture(N, M, map_grid)