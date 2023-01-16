function solution(dartResult) {
  let num = 0;
  const arr = [];
  for (let i = 0; i < dartResult.length; i++) {
    if (/^[0-9]+$/.test(dartResult[i])) {
      dartResult[i - 1] === '1' ? (num = 10) : (num = Number(dartResult[i]));
    } else if (dartResult[i] === 'S') arr.push(num);
    else if (dartResult[i] === 'D') arr.push(num * num);
    else if (dartResult[i] === 'T') arr.push(num * num * num);
    else if (dartResult[i] === '*') {
      arr[arr.length - 1] = arr[arr.length - 1] * 2;
      arr[arr.length - 2] = arr[arr.length - 2] * 2;
    } else if (dartResult[i] === '#') arr[arr.length - 1] = arr[arr.length - 1] * -1;
  }
  return arr.reduce((acc, cur) => (acc += cur));
}
