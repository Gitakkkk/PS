function solution(test) {
  let result = 0;
  for (let i = 1; i <= 4; i++) {
    for (let j = 1; j <= 4; j++) {
      let cnt = 0;
      for (let x = 0; x < test.length; x++) {
        let a = 0;
        let b = 0;
        for (let y = 0; y < 4; y++) {
          if (test[x][y] === i) a = y;
          if (test[x][y] === j) b = y;
        }
        if (a < b) cnt++;
      }
      if (cnt === 3) result++;
    }
  }
  return result;
}

let arr = [
  [3, 4, 1, 2],
  [4, 3, 2, 1],
  [3, 1, 4, 2],
];
console.log(solution(arr));
