function solution(x) {
  const arr = x
    .toString()
    .split('')
    .map((v) => Number(v));
  return x % arr.reduce((acc, cur) => (acc += cur)) === 0 ? true : false;
}
