function solution(s) {
  const arr = s.split(' ');
  const max = Math.max(...arr);
  const min = Math.min(...arr);
  let result = [];
  result.push(min);
  result.push(max);
  return result.join(' ');
}
