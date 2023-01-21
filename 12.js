function solution(n) {
  let result = n;
  for (let i = 1; i <= n; i++) {
    if (n % i === 1) {
      if (i < result) result = i;
    }
  }
  return result;
}
