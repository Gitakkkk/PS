function solution(n, m) {
  let result = [0, 0];
  let min = 0;
  let max = [];
  for (let i = 1; i <= m; i++) {
    if (n % i === 0) max.push(i);
    if (m % i === 0) {
      if (max[max.length - 1] === i) {
        result[0] = i;
      }
      max.push(i);
    }
  }
  result[1] = (n * m) / result[0];
  return result;
}
