from collections import deque

# 북쪽 나라의 도로

def main(data):
    if not data:  # 입력이 없는 경우
        print(0)
        return
        
    # 도시 번호의 최대값
    city_size = max(max(row[0], row[1]) for row in data)
    
    # 그래프 구성
    graph = [[] for _ in range(city_size + 1)]
    for start, end, weight in data:
        graph[start].append((end, weight))
        graph[end].append((start, weight))
    
    def bfs(start):
        visited = [False] * (city_size + 1)
        dist = [0] * (city_size + 1)
        queue = deque([start])
        visited[start] = True
        
        while queue:
            city = queue.popleft()
            for end, weight in graph[city]:
                if not visited[end]:
                    visited[end] = True
                    dist[end] = dist[city] + weight
                    queue.append(end)
        
        # 가장 먼 노드와 거리 찾기
        max_dist = 0
        farthest_node = start
        for i in range(1, city_size + 1):
            if dist[i] > max_dist:
                max_dist = dist[i]
                farthest_node = i
        
        return farthest_node, max_dist
    
    # 1번 노드에서 가장 먼 노드 찾기
    farthest_node, _ = bfs(1)
    
    # 가장 먼 노드에서 다시 가장 먼 노드 찾기 (트리의 지름)
    _, diameter = bfs(farthest_node)
    
    print(diameter)

data = []
while True:
    try:
        line = input().strip()
        if not line:  # 빈 줄이면 종료
            break
        # 입력 형식 검증
        try:
            start, end, weight = map(int, line.split())
            if start <= 0 or end <= 0 or weight <= 0:  # 음수나 0이 있는 경우
                continue
            data.append([start, end, weight])
        except ValueError:  # 잘못된 입력 형식
            continue
    except EOFError:
        break

main(data)