function solution(topping) {
  const n = topping.length;

  const left = new Set();
  const right = new Map();

  // 오른쪽 부분에 있는 토핑 종류의 수 세팅
  for (let i = 0; i < n; i++) {
    right.set(topping[i], (right.get(topping[i]) || 0) + 1);
  }

  let answer = 0;

  // 0번부터 한번씩 잘라보기
  for (let i = 0; i < n - 1; i++) {
    // 왼쪽 부분에 토핑 추가
    left.add(topping[i]);

    // 오른쪽 부분에서 해당 토핑 하나 제거
    right.set(topping[i], right.get(topping[i]) - 1);
    if (right.get(topping[i]) === 0) {
      right.delete(topping[i]);
    }

    // 왼쪽과 오른쪽의 토핑 종류가 동일하면 카운트 증가
    if (left.size === right.size) {
      answer++;
    }
  }

  return answer;
}
