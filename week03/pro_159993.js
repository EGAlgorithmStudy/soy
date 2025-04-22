function solution(maps) {
  // 미로의 크기
  const N = maps.length;
  const M = maps[0].length;

  // 상, 하, 좌, 우
  const directions = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];

  function bfs(start, target) {
    const queue = [[start[0], start[1], 0]]; // 큐에 [x, y, 거리] 형태로 넣기
    const visited = Array.from(Array(N), () => Array(M).fill(false)); // 방문 배열
    visited[start[0]][start[1]] = true;

    while (queue.length > 0) {
      const [x, y, dist] = queue.shift();

      // 목표 지점에 도달하면 거리 반환
      if (x === target[0] && y === target[1]) {
        return dist;
      }

      // 4방향 이동
      for (const [dx, dy] of directions) {
        const nx = x + dx;
        const ny = y + dy;

        // 미로 범위 내이고, 벽이 아니고, 방문하지 않았다면
        if (
          nx >= 0 &&
          ny >= 0 &&
          nx < N &&
          ny < M &&
          !visited[nx][ny] &&
          maps[nx][ny] !== 'X'
        ) {
          visited[nx][ny] = true;
          queue.push([nx, ny, dist + 1]);
        }
      }
    }
    return -1; // 목표 지점 못가면 -1 반환
  }

  // S, L, E의 위치 찾기
  let start, lever, exit;
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (maps[i][j] === 'S') start = [i, j];
      if (maps[i][j] === 'L') lever = [i, j];
      if (maps[i][j] === 'E') exit = [i, j];
    }
  }

  // 출발점에서 레버까지의 거리
  const distToLever = bfs(start, lever);
  if (distToLever === -1) return -1; // 레버 못가면 -1

  // 레버에서 출구까지의 거리
  const distToExit = bfs(lever, exit);
  if (distToExit === -1) return -1; // 출구 못가면 -1

  // 거리 합
  return distToLever + distToExit;
}
