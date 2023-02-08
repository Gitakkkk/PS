function solution(x, n) {
  const result = [];
  result.push(x);
  for (let i = 2; i <= n; i++) {
    result.push(result[result.length - 1] + x);
  }
  return result;
}
