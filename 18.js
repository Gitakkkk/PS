function solution(absolutes, signs) {
  const array = [];
  for (let i = 0; i < absolutes.length; i++) {
    signs[i] ? array.push(absolutes[i]) : array.push(absolutes[i] * -1);
  }
  return array.reduce((acc, cur) => (acc += cur));
}
