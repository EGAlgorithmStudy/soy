// hash 문제. 의상
function solution(clothes) {
  const categories = new Map(); // 의상 종류와 그에 속한 의상의 수
  let answer = 1; // 최소 1개의 의상을 입을 수 있는 경우

  // 의상 종류별로 의상의 개수를 세기
  for (let i = 0; i < clothes.length; i++) {
    const category = clothes[i][1]; // 의상 종류
    if (categories.has(category)) {
      const count = categories.get(category) + 1;
      categories.set(category, count); // 의상 종류별로 개수 증가
    } else {
      categories.set(category, 1); // 새로운 의상 종류 추가
    }
  }

  // 각 의상 종류에서 선택할 수 있는 개수는 의상 수 + 1
  // 그 의상을 선택하지않는케이스
  categories.forEach((count) => {
    answer *= count + 1; // 각 종류마다 선택할 수 있는 경우의 수를 곱함
  });

  // 최소 1개의 의상은 입어야 함
  return answer - 1;
}
