function solution(s) {
  let arr = [];
  let result = 0;

  for (let i = 0; i < s.length; i += 1) {
    arr.push(s[i]);

    const same = arr.filter((v) => v === arr[0]);
    const notSame = arr.filter((v) => v !== arr[0]);

    if (same.length === notSame.length) {
      result++;
      arr = [];
    }
  }

  if (arr.length !== 0) {
    result++;
  }

  return result;
}
