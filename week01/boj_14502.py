from collections import deque

# 상, 우, 하, 좌 
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# BFS
def spread_virus(map_grid, N, M):
    # 맵 복사
    temp_map = [row[:] for row in map_grid]
    queue = deque()

    # 바이러스 추가
    for i in range(N):
        for j in range(M):
            if temp_map[i][j] == 2:  # 바이러스가 있는 곳
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and temp_map[nx][ny] == 0:
                temp_map[nx][ny] = 2  # 바이러스 퍼짐
                queue.append((nx, ny)) # 바이러스 새거 추가

    # 안전 영역 카운팅
    safe_area = sum(1 for i in range(N) for j in range(M) if temp_map[i][j] == 0)
    return safe_area

# 벽을 3개 세운 후 안전 영역의 최대 크기 계산
def find_max_safe_area(map_grid, N, M):
    max_safe_area = 0
    empty_spaces = [(i, j) for i in range(N) for j in range(M) if map_grid[i][j] == 0] # 빈 좌표 배열로 저장

    def build_wall(wall_count, start_idx):
        nonlocal max_safe_area
        if wall_count == 3:  # 벽 3개를 세운 경우
            max_safe_area = max(max_safe_area, spread_virus(map_grid, N, M))
            return
        
        for idx in range(start_idx, len(empty_spaces)):
            x, y = empty_spaces[idx]
            map_grid[x][y] = 1 
            build_wall(wall_count + 1, idx + 1)
            map_grid[x][y] = 0  

    build_wall(0, 0)
    return max_safe_area

# 메인 함수
def main():
    N, M = map(int, input().split())
    map_grid = [list(map(int, input().split())) for _ in range(N)]
    
    max_safe_area = find_max_safe_area(map_grid, N, M)
    print(max_safe_area)


main()
