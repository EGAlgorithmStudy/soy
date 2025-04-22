// hash 문제. 전화번호 목록
function solution(phone_book) {
  const hash = new Set();
  phone_book.sort((a, b) => a - b);

  for (let phone of phone_book) {
    for (let i = 1; i <= phone.length; i++) {
      const prefix = phone.substring(0, i);
      if (hash.has(prefix)) {
        return false;
      }
    }

    hash.add(phone);
  }

  return true;
}
