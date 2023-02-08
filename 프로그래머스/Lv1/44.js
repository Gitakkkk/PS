function solution(n) {
  const arr = [];
  let result = 0;
  for (let i = 2; i <= n; i++) arr[i] = i;
  for (let i = 2; i <= n; i++) {
    if (arr[i] === 0) continue;
    for (let j = 2 * i; j <= n; j += i) {
      arr[j] = 0;
    }
  }
  for (let i = 2; i < arr.length; i++) {
    if (arr[i] !== 0) result++;
  }
  return result;
}
