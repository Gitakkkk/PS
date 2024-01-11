function solution(a, b) {
  if (a === b) return a;
  const arr = [a, b].sort((a, b) => a - b); // Math.min & max가 더 빠름
  let result = 0;
  for (let i = arr[0]; i <= arr[1]; i++) {
    result += i;
  }
  return result;
}
