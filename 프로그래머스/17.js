function solution(arr, divisor) {
  const array = arr.sort((a, b) => a - b);
  const result = [];
  array.map((v) => {
    v % divisor === 0 ? result.push(v) : null;
  });
  result.length > 0 ? null : result.push(-1);
  return result;
}
