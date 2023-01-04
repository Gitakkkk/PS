function solution(n) {
  const num = n.toString(3).split('').reverse().join('');
  return Number.parseInt(num, 3);
}
